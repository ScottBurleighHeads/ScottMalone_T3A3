from models.User_table import User
from main import db
from flask import Blueprint, jsonify
from schemas.UserSchema import user_schema, users_schema
endpoint = Blueprint("endpoint",__name__)

@endpoint.route("/",methods = ["GET"])
def user_details():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

# @endpoint.route("/")
# def home_page():

#     return jsonify({
#                 "page":"homepage",
#                 "data":[1,2,3,4]
#     })

# # @endpoint.route("/words")
# # def word_page():
