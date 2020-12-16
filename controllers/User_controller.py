from main import db
from flask import Blueprint, jsonify, request
from models.User_table import User
from schemas.User_Schema import user_schema, users_schema
user = Blueprint("user",__name__,url_prefix="/user")

@user.route("/",methods = ["GET"])
def all_information():

    users = User.query.all()
    return jsonify(users_schema.dump(users))

@user.route("/<int:id>",methods=["GET"])
def user_find(id):
    
    user = User.query.get(id)
    return jsonify(user_schema.dump(user))
     

@user.route("/create",methods = ["POST"])
def user_details():
    
    user_fields = user_schema.load(request.json)

    new_user = User()
    new_user.email = user_fields["email"]
    new_user.first_name = user_fields["first_name"]
    new_user.Surname = user_fields["Surname"]
    new_user.Password = user_fields["Password"]
    new_user.Age = user_fields["Age"]
    new_user.Address = user_fields["Address"]
    new_user.City = user_fields["City"]
    new_user.State = user_fields["State"]
    new_user.Country = user_fields["Country"]
    new_user.Postcode = user_fields["Postcode"]
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))

@user.route("/update/<int:id>", methods=["PUT","PATCH"])
def user_update(id):
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(id=id)
    user.update(user_fields)
    db.session.commit()
    
    return jsonify(user_schema.dump(user))

@user.route("/delete/<int:id>", methods=["DELETE"])
def user_delete(id):
    
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))