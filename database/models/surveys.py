from database.config import db

class Survey(db.Model):
    __tablename__ = "Survey"

    survey_id = db.Column(db.Integer, primary_key=True)
    cohort = db.Column(db.Text)
    test = db.Column(db.Text)
    file = db.Column(db.Text)
    start = db.Column(db.Integer)
