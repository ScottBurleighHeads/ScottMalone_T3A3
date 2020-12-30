from flask_sqlalchemy import SQLAlchemy

db = None

def init_db(app):                #It need the main app instance so we need to pass it in, in the main.
    db = SQLAlchemy(app)        # Magic cool connection of the database
    return db


