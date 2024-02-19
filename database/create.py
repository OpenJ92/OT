from database.models.answers import Answers
from database.models.questions import Questions
from database.models.surveys import Survey

from database.config import db

if __name__ == "__main__":
    db.create_all()
