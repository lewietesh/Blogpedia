from main import db,app,login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader

def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    __tablename__ = "users"

    def __init__(self,username,email,password_hash,profile_picture,verified_email,bio_summary,country):
       self.username =username
       self.email = email
       self.password_hash =password_hash
       self.profile_picture =profile_picture
       self.verified_email =verified_email
       self.country = country 


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64), unique= True)
    email = db.Column(db.String(64), unique = True,index =True)
    password_hash = db.Column(db.String(128))
    profile_picture = db.Column(db.String(40))
    verified_email = db.Column(db.Boolean)
    bio_summary  = db.Column(db.String())
    country = db.Column(db.String())
    
    def check_password(self,password):
            return check_password_hash(self.password_hash,password )

    def __repr__(self):
            return f"User('{self.username}', '{self.email}')"
