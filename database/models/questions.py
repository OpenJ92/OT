from database.config import db

class Question(db.Model):
    __tablename__  = "Question"
    __table_args__ = {"schema": "raw"}

    __id__   = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
