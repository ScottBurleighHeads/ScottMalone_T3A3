from main import db 
from models.Tracks_table import Tracks
from models.Playlist_table import playlist

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320),nullable=False, unique=True)
    Password = db.Column(db.String(400),nullable=False)
    first_name = db.Column(db.String(50))
    Surname = db.Column(db.String(50))
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(100))
    City = db.Column(db.String(50))
    State = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Postcode = db.Column(db.Integer)
    subscriptions = db.relationship(Tracks,secondary= playlist,backref=db.backref('subscribers',lazy='dynamic'))
