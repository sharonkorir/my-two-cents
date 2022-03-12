from enum import unique
from . import db

class Quote: 
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote

#user class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = False)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'