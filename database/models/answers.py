from database.config import db

class Answer(db.Model):
    __tablename__  = "Answer"

    answer_id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
