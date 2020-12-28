from models.User_table import User
from models.Tracks_table import Tracks
from main import bcrypt
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.User_Schema import user_schema, users_schema
playlist = Blueprint("playlist",__name__,url_prefix="/playlist")

# Get the users playlist from a many to many relationship
@playlist.route("/<int:id>",methods=["GET"] )
def get_playlist(id):
   
    user1 = User.query.filter_by(id = id).first()
    playlist = []
    try:
        for tracks in user1.playlist:
            playlist.append(tracks.tracks_name)
            user_playlist = {f"{user1.first_name}s playlist":playlist}
        return user_playlist
    except: 
        return f"<h3>ERROR: {user1.first_name} does not have a playlist</h3>"

# @playlist.route("/add_track",methods=["POST"])
# def add_track():
    
#     # user_fields = user_schema.load(request.json)
#     # user = User.query.filter_by(email=user_fields["email"]).first()

#     # if not user or not bcrypt.check_password_hash(user.Password, user_fields["Password"]):
#     #     return abort(401, description="Incorrect username and password")

#     user_id = get_jwt_identity()


    
#     return "hello"