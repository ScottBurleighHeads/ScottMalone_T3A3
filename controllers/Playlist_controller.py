from models.User_table import User
from models.Tracks_table import Tracks
from main import bcrypt
from main import db
from flask import Blueprint, request, jsonify, abort, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.User_Schema import user_schema, users_schema
from schemas.Tracks_Schema import track_schema, tracks_schema
playlist = Blueprint("playlist",__name__,url_prefix="/playlist")

# Get the users playlist from a many to many relationship
@playlist.route("/<int:id>",methods=["GET"] )
def get_playlist(id):
   
    user1 = User.query.filter_by(id = id).first()
    return render_template("playlist.html",user = user1,title = playlist)
    # play = []
    # try:
    #     # for tracks in user1.playlist:
    #     #     play.append(tracks.tracks_name)
    #     #     user_playlist = {f"{user1.first_name}s playlist":play}
    #     # return user_playlist

    # except: 
    #     return f"<h3>ERROR: {user1.first_name} does not have a playlist</h3>"


# Add a track to the users playlist
@playlist.route("/add_track",methods=["POST"])
@jwt_required
def add_track():
    
    # Using the JWT token once a user has logged in they can then change there playlist and only there playlist.
    # Without the JWT token the user will not be aloud to make changes. This technique is 
    # authorizing only the owner of the playlist to make changes to the playlist.
    print(request.json)
    tracks_field = track_schema.load(request.json)
    user_id = get_jwt_identity() # Gets the bearer token.
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    track = Tracks.query.filter_by(tracks_id=tracks_field["tracks_id"]).first()
    
    track.playlist.append(user)
    db.session.commit()

    return {"User": f"{user.first_name} {user.Surname}","New track added":f"{track.tracks_name}","Playlist":f"{get_playlist(user.id)[f'{user.first_name}s playlist']}"}

# delete a track from the users playlist.
@playlist.route("/delete_track", methods=['DELETE'])
@jwt_required
def delete_track():
    tracks_field = track_schema.load(request.json)
    track = Tracks.query.filter_by(tracks_id=tracks_field['tracks_id']).first()
    track_name = track.tracks_name
   
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    user_name = user.first_name + " " + user.Surname

    track.playlist.remove(user)
    db.session.commit()

    return f'{track_name} was removed from {user_name} playlist'