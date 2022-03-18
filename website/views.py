#stores routes not relating to authenication whre user can naviagte too

from flask import Blueprint, render_template, request
from .models import medication
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class medication(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     name = db.Column("name", db.String(100))
#     symptom = db.Column("symptom", db.String(100))


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

@views.route('/medication', methods=['GET','POST'])
def medication():
    if request.method == 'POST':
        medTitle = request.form['med']
        with open('medicationPrice.txt','w') as f:
            f.write(medTitle)
            
    return render_template("medication.html")

@views.route('/guide')
def guide():
    return render_template("guide.html")





