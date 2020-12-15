from main import db 

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320))
    first_name = db.Column(db.String(50))
    Surname = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    Age = db.Column(db.Integer)
    Address = db.Column(db.String(100))
    City = db.Column(db.String(50))
    State = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Postcode = db.Column(db.Integer)
