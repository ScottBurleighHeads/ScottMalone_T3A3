from main import ma
from models.Albums_table import Album

class AlbumsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Album

album_schema = AlbumsSchema()
albums_schema = AlbumsSchema(many=True)