from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
from static.database.databases import get_db
from recommendation import get_recommendation

import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)
app = Flask(__name__)

# Configure session to use signed cookies
app.secret_key = "superawesomesecretkey"

# This will store session data in the server's memory
app.config["SESSION_TYPE"] = "filesystem"

# Initialize the extension
Session(app)


@app.route("/")
def index():
    if "user" in session:
        return render_template("home.html", user=session["user"])
    else:
        # return redirect(url_for("login"))
        return render_template("Main.html")


@app.route("/login")
def login():
    if "user" in session:
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/signup")
def signup():
    if "user" in session:
        return redirect(url_for("home"))
    else:
        return render_template("signup.html")


@app.route("/home")
def home():
    if "user" in session:
        username = session["user"].capitalize()
        db = get_db()
        recommended_roles = db.get_recommended_roles(username)
        summary = "Your recommended roles based on your skillset are: "
        if recommended_roles:
            return render_template(
                "home.html",
                user=username,
                recommendations=recommended_roles,
                summary=summary,
            )
        return render_template("home.html", user=username)
    else:
        return redirect(url_for("login"))


@app.route("/createaccount", methods=["POST"])
def create_account():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    db = get_db()
    others = db.fetch(username)
    if others:
        flash("Username already exists", "error")
        return redirect(url_for("signup"))
    else:
        if len(password) < 8:
            flash("Password must be at least 8 characters long", "error")
            return redirect(url_for("signup"))
        else:
            try:
                db.insert(username, email, password)
                flash("Account created successfully, please login", "success")
                return redirect(url_for("login"))
            except:
                flash("An error occurred", "error")
                return redirect(url_for("signup"))


@app.route("/login_account", methods=["POST"])
def login_account():
    username = request.form["username"]
    password = request.form["password"]
    db = get_db()
    user = db.login(username, password)
    if user:
        # Store the username in the session
        session["user"] = username
        return redirect(url_for("home"))
    else:
        flash("Incorrect username or password", "error")
        return redirect(url_for("login"))


@app.route("/logout", methods=["POST"])
def logout():
    # Clear the session
    session.pop("user", None)
    return redirect(url_for("index"))


@app.route("/create_profile")
def create_profile():
    if "user" in session:
        db = get_db()
        skills = db.get_skills()
        return render_template(
            "create_profile.html", user=session["user"].capitalize(), skills=skills
        )
    else:
        return redirect(url_for("login"))


@app.route("/predict", methods=["POST"])
def predict_career():
    try:
        db = get_db()
        preferences = [x for x in request.form.values()]
        recommendations = get_recommendation(preferences)
        username = session["user"]
        for i in range(len(recommendations)):
            try:
                db.insert_recommended_roles(username, recommendations[i], i + 1)
            except Exception as e:
                logging.error(str(e))  # Log the specific error
                # flash("An error occurred while saving recommended roles. Please try again later.", "error")
                return redirect(url_for("create_profile"))
        return redirect(url_for("home"))
    except Exception as e:
        logging.error(str(e))  # Log the specific error
        flash("An error occurred while processing your request. Please try again later.", "error")
if __name__ == "__main__":
    app.run(debug=True)