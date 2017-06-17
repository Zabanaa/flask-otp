from flask import Blueprint

auth    = Blueprint("auth", __name__)

@auth.route("/register")
def register_user():
    return "register blud"
