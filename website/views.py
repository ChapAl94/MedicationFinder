#stores routes not relating to authenication whre user can naviagte too

from flask import Blueprint, render_template, request, flash, url_for, redirect
from .models import medicationBrand
from . import db
import time


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/symptoms' , methods = ['GET', 'POST'])
def symptoms():
    if request.method == 'POST':
        print(request.form.get('symptomCheckBox'))
        return 'Done'
    return render_template("symptoms.html")


@views.route('/newMed', methods = ['GET','POST'])
def newMed():
    if request.method == 'POST':
        new_medicine = medicationBrand(request.form['name'], request.form['treatment'],request.form['storeLocation'], request.form['cost'])
        db.session.add(new_medicine)
        db.session.commit()
        flash('Medicine has been added')
        return redirect(url_for('views.medication'))
    return render_template("newMed.html")


@views.route('/medication', methods=['GET','POST'])
def medication():
    if request.method == 'POST':
        medTitle = request.form['med']
        with open('medicationPrice.txt','w') as f:
            f.write(medTitle)
        
        time.sleep(10)

        with open('medicationPrice.txt','r') as f:
            priceMed = f.read()
            return priceMed
    return render_template("medication.html")

@views.route('/guide')
def guide():
    return render_template("guide.html")





