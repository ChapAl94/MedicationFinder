from . import db 
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()


class medication(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    medicationName = db.Column(db.String(100))
    symptom = db.Column(db.String(100))
    location = db.Column(db.String(100))

    # def __init__(self, medicationName, symptom, location):
    #     self.medicationName = medicationName
    #     self.symptom = symptom
    #     self.location = location

# meds1 = medication("Tynenol", "pain, headache, fever", "Walgreens, Somerville, MA")
# meds2 = medication("Advil", "pain, headache, fever", "CVS, Lowell, MA")
# meds3 = medication("Zyrtec", "allergies", "Walmart, Cambridge, MA")
# meds4 = medication("Benadryl", "allergies", "Walgreens, Somerville, MA")
# meds5 = medication("Pepto Bismol", "stomach ache, diahrea", "Walgreens, Boston, MA")
# meds6 = medication("Alieve", "pain, headache, fever", "Walgreens, Somerville, MA")
# meds7 = medication("Tynenol", "pain, headache, fever", "Walgreens, Somerville, MA")

