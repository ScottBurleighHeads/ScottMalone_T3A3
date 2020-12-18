from main import db
from flask import Blueprint, jsonify, request
from models.Artist_table import Artist
from sqlalchemy import text,func
from schemas.Artist_Schema import artist_schema, artists_schema

artist = Blueprint("artist",__name__,url_prefix="/artist")

@artist.route("/")
def hello():
    return "Hello world"

# Finds the artist that made the most money using the MAX sequel query and displays in a dictionary.
@artist.route("/Highest_profit")
def max_profit():
    
    max_pay = db.session.query(func.max(Artist.gross_worth)).scalar()
    artist_name = Artist.query.filter_by(gross_worth=max_pay).first()
    max_pay = {"Highest paid amount":f"${max_pay}", "name":artist_name.Artist_name}
    return max_pay

# Finds the artist that made the least money using the MAX sequel query and displays in a dictionary.
@artist.route("/Lowest_profit")

def min_profit():
    
    min_pay = db.session.query(func.min(Artist.gross_worth)).scalar()
    artist_name = Artist.query.filter_by(gross_worth=min_pay).first()
    min_pay = {"Lowest paid amount":f"${min_pay}", "name":artist_name.Artist_name}
    
    return min_pay

# Finds the average profit of all artists fullfilling the average requirement. 
@artist.route("/Average_profit")
def Average_profit():

    average_pay_query = int(db.session.query(func.avg(Artist.gross_worth)).scalar())
    average_pay = {"Average gross payment": f"${average_pay_query}"}
    return average_pay




