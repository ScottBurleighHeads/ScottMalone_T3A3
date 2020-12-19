from main import ma
from models.Albums_table import Album

class AlbumsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Album
    
    album_name = ma.String(required=True)
    # date_released = ma.Datetime(required=True)

album_schema = AlbumsSchema()
albums_schema = AlbumsSchema(many=True)