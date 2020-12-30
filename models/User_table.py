from main import db 
from models.Tracks_table import Tracks
from models.Playlist_table import playlist
from models.Alias_table import Alias

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320),nullable=False, unique=True)
    password = db.Column(db.String(400),nullable=False)
    first_name = db.Column(db.String(50))
    Surname = db.Column(db.String(50))
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(100))
    City = db.Column(db.String(50))
    State = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Postcode = db.Column(db.Integer)
    token = db.Column(db.String(500))
    playlist = db.relationship(Tracks,secondary=playlist,backref=db.backref('playlist', lazy='dynamic'),cascade="all, delete")
    alias = db.relationship(Alias, backref="user_alias", uselist=False) #uselist=False makes the table one to one.