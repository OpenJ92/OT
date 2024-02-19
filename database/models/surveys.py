from database.config import db

class Survey(db.Model):
    __tablename__ = "Survey"
    __table_args__ = {"schema": "raw"}

    __id__ = db.Column(db.Integer, primary_key=True)
    cohort = db.Column(db.Text)
    test = db.Column(db.Text)
    file = db.Column(db.Text)
    start = db.Column(db.Integer)

    ## Synthetic table from raw. survey_id, question_id, answer_id
