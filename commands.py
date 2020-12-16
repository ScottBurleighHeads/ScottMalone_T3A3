from flask import Blueprint
from main import db
db_commands = Blueprint("db",__name__)

# from faker import Faker
# fake = Faker()

@db_commands.cli.command("create")
def create_db():
    db.create_all()                     # Create_all() method is from the SQLAlchemy
    print("Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

# @db_commands.cli.command("seed")
# def seed_db():
