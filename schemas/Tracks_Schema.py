from main import ma
from models.Tracks_table import Tracks

class TracksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tracks

track_schema = TracksSchema()
tracks_schema = TracksSchema(many=True)