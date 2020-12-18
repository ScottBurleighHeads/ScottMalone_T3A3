from main import db
from flask import Blueprint, jsonify, request
from models.Artist_table import Artist
from sqlalchemy import text,func
from schemas.Artist_Schema import artist_schema, artists_schema

artist = Blueprint("artist",__name__,url_prefix="/artist")

# The endpoints below will meet the requiements of R7(MIN,MAX,AVERAGE,SUM) and R10(Three queries filtering,ordering and selecting)

@artist.route("/")
def hello():
    return "Hello artist"

# Finds the artist that made the most money using the MAX sequel query and displays in a dictionary. Requirement ()
@artist.route("/Highest_profit")
def max_profit():
    
    max_pay = db.session.query(func.max(Artist.gross_worth)).scalar()
    artist_name = Artist.query.filter_by(gross_worth=max_pay).first()                # (1/3) R10) filtering requirements. This is selecting.
    max_pay = {"Highest paid amount":f"${max_pay}", "name":artist_name.Artist_name}  # Selected artist name that earned the most profit.
    return max_pay

# Finds the artist that made the least money using the MAX sequel query and displays in a dictionary.
@artist.route("/Lowest_profit")

def min_profit():
    
    min_pay = db.session.query(func.min(Artist.gross_worth)).scalar()
    artist_name = Artist.query.filter_by(gross_worth=min_pay).first()
    min_pay = {"Lowest paid amount":f"${min_pay}", "name":artist_name.Artist_name}
    
    return min_pay

# Calculates the average profit of all artists fullfilling the average requirement. 
@artist.route("/Average_profit")
def Average_profit():

    average_pay_query = int(db.session.query(func.avg(Artist.gross_worth)).scalar())
    average_pay = {"Average gross payment": f"${average_pay_query}"}
    return average_pay
# Calculates the sum of profit from all artist 
@artist.route("/Sum_profit")
def Sum_profit():

    sum_pay_query = int(db.session.query(func.sum(Artist.gross_worth)).scalar())
    sum_pay = {"Sum of all artists": f"${sum_pay_query}"}
    return sum_pay

# (2/3) R10) Filtering requirements. Prints the table contents into an API by the order from  largest gross_worth to smallest using gross_worth table.
@artist.route("/Ordering") 
def Order_by_profit():

    ordering =  Artist.query.order_by(Artist.gross_worth.desc()).all()
    return jsonify(artists_schema.dump(ordering))

# (3/3) R10) Prints the table contents into an API where any artist that earns $40 000 000 will be displayed.
@artist.route("/filtering")
def Filter_by_profit():

    filtering = Artist.query.filter((Artist.gross_worth < 40000000)).all()
    return jsonify(artists_schema.dump(filtering))