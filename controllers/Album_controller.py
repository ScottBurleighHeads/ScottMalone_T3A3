from main import db
from flask import Blueprint, jsonify, request
from models.Albums_table import Album
from schemas.Albums_Schema import album_schema, albums_schema
album = Blueprint("albums",__name__,url_prefix="/albums")


@album.route("/")
def Hello():
    return "hello"