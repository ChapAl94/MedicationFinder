from . import db 



class medication(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    medicationName = db.Column(db.String(100))
    symptom = db.Column(db.String(100))
    location = db.Column(db.String(100))

    # def __init__(self, medicationName, symptom, location):
    #     self.medicationName = medicationName
    #     self.symptom = symptom
    #     self.location = location