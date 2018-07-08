import os

from flask import Flask, render_template, request, session
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
engine = create_engine(os.getenv("postgres://pezufjjvmkmciq:c0798f396cc8f2813bbbd08c28c9833260c3274ba4ff15670c93bac5b3777c1c@ec2-23-23-93-115.compute-1.amazonaws.com:5432/d2ujn0f3h1cj9j"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    return render_template("success.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template("results.html", message="You are logged in and results are coming soon!")