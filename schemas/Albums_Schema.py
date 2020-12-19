from main import ma
from models.Albums_table import Album
from marshmallow.validate import Length


class AlbumsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Album
    
    album_name = ma.String(required=False, validate=Length(min=1,max=100))
    date_released = ma.DateTime(required=True)

album_schema = AlbumsSchema()
albums_schema = AlbumsSchema(many=True)