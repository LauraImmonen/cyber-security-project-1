from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config['DEBUG'] = True
    db.init_app(app)