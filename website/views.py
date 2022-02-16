#stores routes not relating to authenication whre user can naviagte too

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/symptoms')
def symptoms():
    return render_template("symptoms.html")

@views.route('/medication')
def medication():
    return render_template("medication.html")

@views.route('/guide')
def guide():
    return render_template("guide.html")





