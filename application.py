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
    if db.execute("SELECT * FROM users WHERE username = :username AND password = :password",
                      {"username": username, "password": password}).rowcount == 0:
        return render_template("error.html", message="Invalid login.")

    # Login is valid, so take user to results page.
    db.commit()
    return redirect("/search")

@app.route("/search")
def search():
    """Search for a location."""

    return render_template("search.html")