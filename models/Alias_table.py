from main import db

class Alias(db.Model):
    __tablename__ = "alias"

    alias_id = db.Column(db.Integer, primary_key=True)
    alias_name = db.Column(db.String(50),unique=True) 
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
