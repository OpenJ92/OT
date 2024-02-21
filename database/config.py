from flask import Flask
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
server.config[ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///instance/ot.db"
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)
