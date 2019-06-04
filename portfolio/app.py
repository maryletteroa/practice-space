# -*- coding: utf-8 -*-
# @Author: Marylette B. Roa
# @Date:   2019-06-04 15:13:18
# @Last Modified by:   Marylette B. Roa
# @Last Modified time: 2019-06-04 15:30:16

from flask import Flask
from flask import render_template

from random import randint

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/skills/", defaults= {"username": None})
@app.route("/skills/<string:username>/")
def skills(username):
    return render_template("skills.html", username=username)

@app.route("/projects/")
def projects():
    projects = ["Facebook", "Twitter", "Instagram", "Uber", "Grab"]
    randNo = randint(0, len(projects)-1)
    project = projects[randNo]
    return render_template("projects.html", **locals())

@app.route("/contact/")
def contact():
    return render_template("contact.html")