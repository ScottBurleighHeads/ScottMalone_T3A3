from main import ma
from models.playlist_table import playlist

class PlaylistSchema(ma.SQLAchemyAutoSchema):
    class Meta:
        model = playlist

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)