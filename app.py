from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from db import db, init_db
from main_route import main_routes


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
init_db(app)
app.register_blueprint(main_routes)

if __name__ == "__main__":
    app.run()
