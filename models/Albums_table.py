from main import db
from models.Artist_table import Artist

class Album(db.Model):
    __tablename__ = 'album'

    album_id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(100))
    date_released = db.Column(db.DateTime)
    Artist_id = db.Column(db.Integer, db.ForeignKey(Artist.Artist_id),nullable=False)

    def __repr__(self):
        return f"<Book {self.album_name}>"