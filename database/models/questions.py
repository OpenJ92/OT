from database.config import db

class Question(db.Model):
    __tablename__  = "Question"

    question_id   = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
