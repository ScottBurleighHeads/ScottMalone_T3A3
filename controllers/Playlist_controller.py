from flask import Blueprint
from models.Playlist_table import Playlist
playlist = Blueprint("playlist",__name__,url_prefix="/playlist")

@playlist.route("/")
def Hello():
    return "hello"

