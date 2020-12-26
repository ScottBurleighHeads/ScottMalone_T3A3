from main import db
from models.Artist_table import Artist
from sqlalchemy import text,func
from schemas.Artist_Schema import artist_schema, artists_schema
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
artist = Blueprint("artist",__name__,url_prefix="/artist")

# The endpoints below will meet the requiements of R7(MIN,MAX,AVERAGE,SUM) and R10(Three queries filtering,ordering and selecting)

# Finds the artist that made the most money using the MAX sequel query and displays in a dictionary. Requirement (R7)
@artist.route("/Highest_profit",methods=["GET"])
@jwt_required
def max_profit():
    
    max_pay = db.session.query(func.max(Artist.gross_worth)).scalar()
    artist_name = Artist.query.filter_by(gross_worth=max_pay).first()                # (1/3) R10) filtering requirements. This is selecting.
    max_pay = {"Highest paid amount":f"${max_pay}", "name":artist_name.Artist_name}  # Selected artist name that earned the most profit.
    return max_pay

# Finds the artist that made the least money using the MAX sequel query and displays in a dictionary. Requirement (R7)
@artist.route("/Lowest_profit",methods=["GET"])
def min_profit():
    
    min_pay = db.session.query(func.min(Artist.gross_worth)).scalar()
    artist_name = Artist.query.filter_by(gross_worth=min_pay).first()
    min_pay = {"Lowest paid amount":f"${min_pay}", "name":artist_name.Artist_name}
    
    return min_pay

# Calculates the average profit of all artists fullfilling the average requirement. Requirement (R7)
@artist.route("/Average_profit",methods=["GET"])
def Average_profit():

    average_pay_query = int(db.session.query(func.avg(Artist.gross_worth)).scalar())
    average_pay = {"Average gross payment": f"${average_pay_query}"}
    return average_pay
# Calculates the sum of profit from all artist Requirement (R7)
@artist.route("/Sum_profit",methods=["GET"])
def Sum_profit():

    sum_pay_query = int(db.session.query(func.sum(Artist.gross_worth)).scalar())
    sum_pay = {"Sum of all artists": f"${sum_pay_query}"}
    return sum_pay

# (2/3) R10) Filtering requirements. Prints the table contents into an API by the order from  largest gross_worth to smallest gross_worth using the table.
@artist.route("/Ordering",methods=["GET"]) 
def Order_by_profit():

    ordering =  Artist.query.order_by(Artist.gross_worth.desc()).all()
    return jsonify(artists_schema.dump(ordering))

# (3/3) R10) Prints the table contents into an API where any artist that earns less then $40 000 000 will be displayed.
@artist.route("/filtering",methods=["GET"])
def Filter_by_profit():

    filtering = Artist.query.filter((Artist.gross_worth < 40000000)).all()
    return jsonify(artists_schema.dump(filtering))

# One to many example of Artist to Albums. Artist is the parent and I was able 
# to find the albums that the artists has create through the relationship 
@artist.route("/<int:id>/Albums",methods=["GET"])
def All_albums(id):
    artist = Artist.query.filter_by(Artist_id=id).first()
    album_list = []
    for item in artist.albums:
        album_list.append(item.album_name)
    if not album_list:
        return f"<h1>Unfortunately {artist.Artist_name} has not deposited any albums yet.</h1>"
    artist_albums = {"Album names": album_list}
    return artist_albums

@artist.route("/<int:id>/Tracks",methods=["GET"])
def All_tracks(id):
    artist = Artist.query.filter_by(Artist_id=id).first()
    tracks_list = []
    for item in artist.tracks:
        tracks_list.append(item.tracks_name)
    if not tracks_list:
        return f"<h1>Unfortunately {artist.Artist_name} has not deposited any tracks yet.</h1>"
    artist_tracks = {"Tracks names": tracks_list}
    return artist_tracks
