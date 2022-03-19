from . import db 


class medicationBrand(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    medicationName = db.Column(db.String(100))
    symptom = db.Column(db.String(100))
    location = db.Column(db.String(100))
    cost = db.Column(db.String(100))

    def __init__(self, medicationName, symptom, location, cost):
        self.medicationName = medicationName
        self.symptom = symptom
        self.location = location
        self.cost = cost



