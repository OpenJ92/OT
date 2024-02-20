from database.config import db

class Survey_Question_Answer(db.Model):
    __tablename__ = " Survey_Question_Answer"
    __table_args__ = {"schema": "raw"}

    __id__ = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer)
    answer_id = db.Column(db.Integer)
