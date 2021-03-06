from main import db
from models.Albums_table import Album
from models.Tracks_table import Tracks

class Artist(db.Model): 
    __tablename__ = "artist"

    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100))
    Country = db.Column(db.String(50))
    gross_worth = db.Column(db.Integer)
    albums = db.relationship(Album, backref='artist_album',cascade = "all, delete")
    tracks = db.relationship(Tracks, backref='artist_track',cascade = "all, delete")

  

