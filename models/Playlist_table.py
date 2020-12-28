from main import db
from sqlalchemy import UniqueConstraint

# Many to many connection between Users and tracks
playlist = db.Table('playlist',
db.Column('tracks_id',db.Integer, db.ForeignKey('tracks.tracks_id'), nullable=False),
db.Column('id',db.Integer, db.ForeignKey('user.id'), nullable=False),
UniqueConstraint('tracks_id','id')
)



