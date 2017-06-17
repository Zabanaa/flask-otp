from otp_flask import db

class User(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(80), unique=True)
    email       = db.Column(db.String(120), unique=True)
    password    = db.Column(db.String(24), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email    = email
        self.password = password

    def hash_password(self):
        pass

    def __repr__(self):
        return "User: {}".format(self.username)

