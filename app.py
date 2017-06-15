from flask import Flask, render_template, request, redirect, jsonify
import pyotp

app         = Flask(__name__)
app.config["SECRET_KEY"] = "SOMERANDOMSEQUENCE"
otp         = pyotp.TOTP(app.config["SECRET_KEY"])
otp_value   = otp.now()


@app.route("/", methods=["GET"])
def index_otp():
    return render_template("index.html", {})

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
