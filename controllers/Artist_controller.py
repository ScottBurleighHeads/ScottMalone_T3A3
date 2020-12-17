from main import db
from flask import Blueprint, jsonify, request
from models.Artist_table import Artist
from schemas.Artist_Schema import artist_schema, artists_schema
artist = Blueprint("artist",__name__,url_prefix="/artist")

@artist.route("/")
def hello():
    return "Hello world"

# Finds the artist that made the most money tak
@artist.route("/")
def max_profit():
    return