import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/newClaim", methods=["GET", "POST"])
def newClaim():
    if request.method == "POST":
        own_damage = "on" if request.form.get("own_damage") else "off"
        claimData = {
            "client_name": request.form.get("client_name"),
            "contact_number": request.form.get("contact_number"),
            "email_address": request.form.get("email_address"),
            "incident_date": request.form.get("incident_date"),
            "liability": request.form.get("liability"),
            "circumstances": request.form.get("circumstances"),
            "registration": request.form.get("registration"),
            "make_and_model": request.form.get("make_and_model"),
            "any_ad": request.form.get("any_ad"),
            "driver_name": request.form.get("driver_name"),
            "dob": request.form.get("dob"),
            "lic_held": request.form.get("lic_held"),
            "date_lic_passed": request.form.get("date_lic_passed"),
            "any_points": request.form.get("any_points"),
            "medical_conditoins": request.form.get("medical_conditoins"),
            "tp_name": request.form.get("tp_name"),
            "tp_number": request.form.get("tp_number"),
            "tp_reg": request.form.get("tp_reg"),
            "tp_veh_make": request.form.get("tp_veh_make"),
            "tp_passnagers": request.form.get("tp_passnagers"),
            "tp_address": request.form.get("tp_address"),
            "tp_email": request.form.get("tp_email"),
        }
        mongo.db.claimForm.insert_one(claimData)
    liability = mongo.db.liability.find().sort("liability", 1)
    flash("Claim Successfully Added!")
    return render_template("newClaim.html", liability=liability)


@app.route("/claims")
def claims():
    claims = mongo.db.claimForm.find()
    return render_template("claims.html", claims=claims)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registraion successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check is username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
        # ensure hashed password matches unser input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # password invalid
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login")) 
        else:
            # username doesn't exist
            flash("Incorrect User name and/or password")
            return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# change this to false when submitting the project
