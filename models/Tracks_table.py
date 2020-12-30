from main import db

class Tracks(db.Model):
    __tablename__ = "tracks"
    
    tracks_id = db.Column(db.Integer, primary_key=True)
    tracks_name = db.Column(db.String(100))
    date_released = db.Column(db.DateTime)
    genre = db.Column(db.String(50))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'),nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'),nullable=False)

    