from models.Artist_table import Artist
from main import db


class Tracks(db.Model):
    __tablename__ = "tracks"
    
    
    tracks_id = db.Column(db.Integer, primary_key=True)
    tracks_name = db.Column(db.String(100))
    date_released = db.Column(db.DateTime)
    genre = db.Column(db.String(50))
    Artist_id = db.Column(db.Integer, db.ForeignKey(Artist.Artist_id),nullable=False)