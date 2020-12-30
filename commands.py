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

# @db_commands.cli.command("seed")
def seed_db():
    from models.User_table import User
    from models.Artist_table import Artist
    from models.Tracks_table import Tracks
    from models.Albums_table import Album
    from flask_jwt_extended import create_access_token
    from datetime import timedelta
    from main import bcrypt
    from faker import Faker
    import random

    fake = Faker()
    length = 10
    expiry = timedelta(days=1)
    for i in range(length):
        user = User()
        user.email = f"test{i}@test.com"
        user.first_name = fake.first_name()
        user.Surname = fake.first_name()
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        user.Age = random.randint(18,60)
        user.Address = fake.address()
        user.City = fake.city()
        user.State = fake.state()
        user.Country = fake.country()
        user.Postcode = random.randint(1000,3000)
        db.session.add(user)
        db.session.commit()
        user.token = create_access_token(identity=str(user.id), expires_delta=expiry)  # JWT Token only for development debugging
    
        db.session.add(user)
        db.session.commit()
            
        artist = Artist()
        artist.artist_name = fake.name()
        artist.Country = fake.country()
        artist.gross_worth = random.randint(50000,50000000)
        db.session.add(artist)
    db.session.commit()
    
    for i in range(length):
        
        album = Album()
        album.album_name = fake.first_name()
        album.date_released = fake.date()
        album.artist_id = random.randint(1,length)
        db.session.add(album)
    db.session.commit()

    for i in range(length):
        
        track = Tracks()
        track.tracks_name = fake.first_name()
        track.date_released = fake.date()
        track.genre = fake.first_name()
        track.artist_id = random.randint(1,length)
        track.album_id = random.randint(1,length)
        db.session.add(track)
    db.session.commit()
    
    for i in range(length*20):
        
        # I have put a unique constraint in the playlist meaning the user cant have the 
        # same track in the the playlist. 

        try:
            track1 = Tracks.query.filter_by(tracks_id=random.randint(1,length)).first()
            user1 = User.query.filter_by(id = random.randint(1,length)).first()
            track1.playlist.append(user1)
            db.session.commit()
        except:
            pass
    
                

@db_commands.cli.command("reset")
def reset_db():
    db.drop_all()
    print("Tables dropped")
    db.create_all()
    print("Tables created")
    seed_db()
    print("Tables seeded")

    
    

