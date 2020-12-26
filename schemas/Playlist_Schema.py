from main import ma
from models.Playlist import Playlist

class PlaylistSchema(ma.SQLAchemyAutoSchema):
    class Meta:
        model = Playlist

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)