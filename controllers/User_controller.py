from models.User_table import User
from schemas.User_Schema import user_schema, users_schema
from main import db
from main import bcrypt
from flask import Blueprint, jsonify, request, abort
user = Blueprint("user",__name__,url_prefix="/user")

# Evidence of building a full crud resource. Point out looking at the methods will determine type of request

@user.route("/login",methods= ["POST"])
def auth_login():
    
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.Password, user_fields["Password"]):
        return abort(401, description="Incorrect username and password")
    
    return "token"

@user.route("/",methods = ["GET"])
def all_information():

    users = User.query.all()
    return jsonify(users_schema.dump(users))

@user.route("/<int:id>",methods=["GET"])
def find_user(id):
    
    user = User.query.get(id)
    return jsonify(user_schema.dump(user))
     

@user.route("/create",methods = ["POST"])
def Create_new_user():
    
    user_fields = user_schema.load(request.json)
    print(user_fields["email"])
    
    user = User.query.filter_by(email=user_fields["email"]).first()
    
    if user:
        return abort(400, description="Email already registered")

    new_user = User()
    new_user.email = user_fields["email"]
    new_user.first_name = user_fields["first_name"]
    new_user.Surname = user_fields["Surname"]
    new_user.Password =  bcrypt.generate_password_hash(user_fields["Password"]).decode("utf-8")
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
def update_user(id):
    
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(id=id)
    user.update(user_fields)
    db.session.commit()

    return jsonify(user_schema.dump(user.first()))

@user.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))