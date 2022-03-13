from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask import flash

class Quote: 
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment',backref = 'posts',lazy = "dynamic")
    slug = db.Column(db.String(255))

    def __repr__(self):
        return f'Post {self.title}'

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = Post.query.order_by(Post.date_posted).all()
        return posts

    @classmethod
    def delete_posts(cls,id):
        post = Post.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()

    @classmethod
    def edit_posts(cls,id):
        post = Post.query.filter_by(post_id=id).update({"content": post.content})
        db.session.commit()

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(225))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))

    def __repr__(self):
        return f'Comment {self.comment}'

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        comments =Comment.query.filter_by(post_id = post_id)
        return comments

    @classmethod
    def delete_comments(cls,id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()