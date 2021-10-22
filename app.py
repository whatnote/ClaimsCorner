import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_claimForm")
def get_claimForm():
    claimForm = mongo.db.claimForm.find()
    return render_template("claimForm.html", claimForm=claimForm)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/newClaim")
def newClaim():
    liability = mongo.db.liability.find().sort("liability", 1)
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

        #put the new user into 'seddion' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registraion successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check is username exists in db?
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure check_password matches use input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get(
                        "username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# change this to false when submitting the project
