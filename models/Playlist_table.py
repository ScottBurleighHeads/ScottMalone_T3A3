from main import db

playlist = db.Table('subs',
                 db.Column('tracks_id',db.Integer, db.ForeignKey('tracks.tracks_id'), nullable=False),
                 db.Column('id',db.Integer, db.ForeignKey('user.id'), nullable=False)
                )

