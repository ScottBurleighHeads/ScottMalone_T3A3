from main import db
from models.Albums_table import Album
class Artist(db.Model): 
    __tablename__ = "artist"

    Artist_id = db.Column(db.Integer, primary_key=True)
    Artist_name = db.Column(db.String(100))
    Country = db.Column(db.String(50))
    gross_worth = db.Column(db.Integer)
    albums = db.relationship('Album', backref='artist_album')
  

