from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User: {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    author = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    published = db.Column(db.Integer, default=0)
    body = db.Column(db.String)

    def __repr__(self):
        return '<Article: {}>'.format(self.title)
