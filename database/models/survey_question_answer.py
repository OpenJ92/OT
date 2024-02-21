from database.config import db

class Survey_Question_Answer(db.Model):
    __tablename__ = " Survey_Question_Answer"

    sqa_id = db.Column(db.Integer, primary_key=True)

    survey_id = db.Column(db.Integer, db.ForeignKey("Survey.survey_id"))
    question_id = db.Column(db.Integer,  db.ForeignKey("Question.question_id"))
    answer_id = db.Column(db.Integer, db.ForeignKey("Answer.answer_id"))
