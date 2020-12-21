from main import ma
from models.User_table import User
from marshmallow import fields
from marshmallow.validate import Length, Range

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["Password"] # wont output the password to the api.
    
    # Validation by specifying datatypes.
    email = ma.Email(required=True)
    first_name = ma.String(required=True, validate=Length(1,50))
    Surname = ma.String(required=True, validate=Length(1,50))
    Password = ma.String(required=True, validate=Length(1,200))
    Age = ma.Integer(required=True, validate=Range(0,150))
    Address = ma.String(required=True, validate=Length(1,100))
    City = ma.String(required=True, validate=Length(1,50))
    State = ma.String(required=True, validate=Length(1,50))
    Country = ma.String(required=True, validate=Length(1,50))
    Postcode = ma.Integer(required=True, validate=Range(1000,9999))
    

user_schema = UserSchema()
users_schema = UserSchema(many=True)

