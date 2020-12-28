from main import db
from sqlalchemy import UniqueConstraint

# Many to Many connection between Users and tracks. Added UniqueConstraint so the same
# track cant be added multiple times.
playlist = db.Table('playlist',
db.Column('id',db.Integer, db.ForeignKey('user.id'), nullable=False),
db.Column('tracks_id',db.Integer, db.ForeignKey('tracks.tracks_id'), nullable=False),
UniqueConstraint('id','tracks_id')
)



