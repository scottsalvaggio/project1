import os

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    """Register for an account."""

    # Get form information.
    username = request.form.get("username")
    password = request.form.get("password")

    # Check if username exists.
    if not db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount == 0:
        return render_template("error.html", message="Username already exists.")

    # Add user credentials to users table.
    db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": username, "password": password})

    # Commit INSERT to users table.
    db.commit()
    return render_template("success.html")

@app.route("/login", methods=["POST"])
def login():
    """Log into website."""

    # Get form information.
    username = request.form.get("username")
    password = request.form.get("password")

    # Check for valid username/password.
    user = db.execute("SELECT * FROM users WHERE username = :username AND password = :password",
                      {"username": username, "password": password}).fetchone()
    if user is None:
        return render_template("error.html", message="Invalid login.")

    # Login is valid, so take user to results page.
    db.commit()
    session["user_id"] = user.id
    return redirect("/search")

@app.route("/search")
def search():
    """Search for a location."""

    return render_template("search.html")

@app.route("/locations", methods=["POST"])
def locations():
    """Show location details."""

    # Get form information.
    zip_code = request.form.get("zip_code")
    city = request.form.get("city")
    zip_length = len(zip_code)
    city_length = len(city)

    # If both values are empty, return error.
    if zip_length == 0 and city_length == 0:
        return render_template("error.html", message="No ZIP code or city entered.")

    # Wrap form values in wildcards if not empty.
    if not zip_length == 0:
        zip_code = '%' + zip_code + '%'
    if not city_length == 0:
        city = '%' + city + '%'

    # Keep track of whether both form values are not empty.
    non_empty_zip_and_city = not zip_length == 0 and not city_length == 0

    # Define SQL query pieces.
    select = "SELECT * FROM locations"
    where1 = " WHERE zip_code LIKE :zip_code"
    where2 = " AND" if non_empty_zip_and_city else " OR"
    where3 = " city ILIKE :city"
    order_by = " ORDER BY city, state, zip_code"

    # Search locations table.
    locations = db.execute(select + where1 + where2 + where3 + order_by,
                           {"zip_code": zip_code, "city": city}).fetchall()
    if len(locations) == 0:
        return render_template("error.html", message="No location found.")

    # Take user to results page.
    db.commit()
    return render_template("locations.html", locations=locations)

@app.route("/locations/<int:location_id>")
def location(location_id):
    """List details about a location."""

    # Make sure location exists.
    location = db.execute("SELECT * FROM locations WHERE id = :id", {"id": location_id}).fetchone()
    if location is None:
        return render_template("error.html", message="No such location.")

    # Get all passengers on that flight, send them to our flight.html template.
    check_ins = db.execute("SELECT users.username, check_ins.comment FROM check_ins \
                            JOIN locations ON check_ins.location_id = locations.id \
                            JOIN users ON check_ins.user_id = users.id WHERE locations.id = :location_id",
                            {"location_id": location_id}).fetchall()
    return render_template("location.html", location=location, check_ins=check_ins)