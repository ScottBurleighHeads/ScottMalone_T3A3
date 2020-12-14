# from database import cursor, connect
from flask import Blueprint, jsonify
endpoint = Blueprint("endpoint",__name__)

@endpoint.route("/")
def home_page():

    return jsonify({
                "page":"homepage",
                "data":[1,2,3,4]
    })

# @endpoint.route("/words")
# def word_page():
