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

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/newClaim")
def newClaim(): 
    return render_template("newClaim.html")

@app.route("/claims")
def claims():
    claims = list(mongo.db.claimForm.find())
    return render_template("claims.html", claims=claims)


@app.route("/register")
def register():
    
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
   return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# change this to false when submitting the project
