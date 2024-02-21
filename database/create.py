from database.models.answers import Answer
from database.models.questions import Question
from database.models.surveys import Survey
from database.models.survey_question_answer import Survey_Question_Answer

from database.config import db
from application.app import app

def create_database():
    with app.server.app_context():
        db.create_all()
