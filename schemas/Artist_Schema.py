from main import ma
from models.Artist_table import Artist

class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artist
    
    # Too save time I only created enpoints with GET request so didnt need to right any input validation.
    # All data input is seeded by the developer.

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)