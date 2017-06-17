from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import pyotp
import os

app             = Flask(__name__)

app.config.from_pyfile( os.path.join(os.getcwd(), "config/main.cfg") )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db              = SQLAlchemy(app)
otp             = pyotp.TOTP(app.config["SECRET_KEY"])
otp_value       = otp.now()

from otp_flask.auth.views import auth
app.register_blueprint(auth, url_prefix="/auth")

@app.route("/", methods=["GET"])
def index_otp():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def process_otp():
    payload     = request.form
    otp_value   = payload["otp_value"]
    verify      = otp.verify(otp_value)

    if verify:
        return redirect("/app")
    else:
        return redirect("/error")

@app.route("/app")
def app_view():
    return "you are validated"

@app.route("/error")
def error_view():
    return "you are not validated"

if __name__ == "__main__":
    app.run(debug=True)
