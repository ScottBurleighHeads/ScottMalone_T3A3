from main import db
from flask import Blueprint, jsonify, request
from models.Tracks_table import Tracks
from schemas.Tracks_Schema import track_schema, tracks_schema
tracks = Blueprint("tracks",__name__,url_prefix="/tracks")


@tracks.route("/")
def Hello():
    return "hello"