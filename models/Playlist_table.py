from models.Tracks_table import Tracks
from models.User_table import User
from main import db

class Playlist(db.Model):
    __tablename__= "playlist"

    playlist_id = db.Column(db.Integer, primary_key=True)
    tracks_id = db.Column(db.Integer, db.ForeignKey(Tracks.tracks_id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

