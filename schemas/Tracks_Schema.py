from main import ma
from models.Tracks_table import Tracks

class TracksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tracks

    # Too save time I only created enpoints with GET request so didnt need to right any input validation.
    # All data input is seeded by the developer. 

track_schema = TracksSchema()
tracks_schema = TracksSchema(many=True)