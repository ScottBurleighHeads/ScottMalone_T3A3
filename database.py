from flask_sqlalchemy import SQLAlchemy
import os

db = None

def init_db(app):                #It need the main app instance so we need to pass it in, in the main.
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://scott:{os.getenv('DB_PASSWORD')}@localhost:5432/t3a3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)        # Magic cool connection of the database
    return db


