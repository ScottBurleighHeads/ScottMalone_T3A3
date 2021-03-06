from main import db
from flask import Blueprint, jsonify, request
from models.Albums_table import Album
from schemas.Albums_Schema import album_schema, albums_schema
album = Blueprint("albums",__name__,url_prefix="/albums")

@album.route("/<int:id>")
def find_album(id):
    album = Album.query.get(id)
    return jsonify(album_schema.dump(album))

@album.route("/update/<int:id>",methods=["PUT","PATCH"])
def update_album(id):
    
    album_fields = album_schema.load(request.json)  # Converts from a JSON file to a dictionary.
    album = Album.query.filter_by(album_id=id)      # Album is of type <class 'flask_sqlalchemy.BaseQuery'> which will equal the raw 
                                                    # sql command to search for Album_id.
    album.update(album_fields)
    db.session.commit()
    return jsonify(album_schema.dump(album.first()))

# One to many Album to tracks relationship. Finds all tracks in Albums.
@album.route("/<int:id>/tracks",methods=["GET"])
def album_tracks(id):
    album = Album.query.filter_by(album_id=id).first()
    tracks_list = []
    for item in album.tracks:
        tracks_list.append(item.tracks_name)
    
    album_tracks = {"Album tracks": tracks_list}
    return album_tracks

