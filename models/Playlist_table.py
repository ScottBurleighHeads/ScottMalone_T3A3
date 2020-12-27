from main import db

playlist = db.Table('playlist',
                 db.Column('tracks_id',db.Integer, db.ForeignKey('tracks.tracks_id'), nullable=False),
                 db.Column('id',db.Integer, db.ForeignKey('user.id'), nullable=False)
                )



