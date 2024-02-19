from database.config import db

class Answer(db.Model):
    __tablename__  = "Answer"
    __table_args__ = {"schema": "raw"}

    __id__ = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)


