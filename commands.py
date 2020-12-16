from flask import Blueprint
from main import db
db_commands = Blueprint("db",__name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()                     # Create_all() method is from the SQLAlchemy
    print("Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_db():
    from models.User_table import User
    from faker import Faker
    import random

    fake = Faker()
    
    for i in range(5):
        user = User()
        user.email = fake.email()
        user.first_name = fake.first_name()
        user.Surname = fake.first_name()
        user.Password = fake.password()
        user.Age = random.randint(18,60)
        user.Address = fake.address()
        user.City = fake.city()
        user.State = fake.state()
        user.Country = fake.country()
        user.Postcode = random.randint(1000+i,3000)
        db.session.add(user)
        db.session.commit()
    print("Table seeded")


