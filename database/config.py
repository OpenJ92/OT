
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
## Rebuild for installable form
server.config[ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///ot.db"
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)
