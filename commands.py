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
    from models.Artist_table import Artist
    from models.Tracks_table import Tracks
    from models.Albums_table import Album
    from main import bcrypt
    from faker import Faker
    import random

    fake = Faker()
    
    for i in range(5):
        user = User()
        user.email = fake.email()
        user.first_name = fake.first_name()
        user.Surname = fake.first_name()
        user.Password = bcrypt.generate_password_hash(fake.password(),8)
        user.Age = random.randint(18,60)
        user.Address = fake.address()
        user.City = fake.city()
        user.State = fake.state()
        user.Country = fake.country()
        user.Postcode = random.randint(1000+i,3000)
        db.session.add(user)
        db.session.commit()

        artist = Artist()
        artist.Artist_name = fake.name()
        artist.Country = fake.country()
        artist.gross_worth = random.randint(50000,50000000)
        db.session.add(artist)
        db.session.commit()

    for i in range(5):
        
        album = Album()
        album.album_name = fake.first_name()
        album.date_released = fake.date()
        album.Artist_id = random.randint(1,4)
        db.session.add(album)
        db.session.commit()

    for i in range(5):
        
        track = Tracks()
        track.tracks_name = fake.first_name()
        track.date_released = fake.date()
        track.genre = fake.first_name()
        track.Artist_id = random.randint(1,4)
        track.album_id = random.randint(1,4)
        db.session.add(track)
        db.session.commit()

    print("Tables seeded")





