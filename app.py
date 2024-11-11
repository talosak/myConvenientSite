import os
import flask
import flask_session
from werkzeug.security import check_password_hash, generate_password_hash

app = flask.Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
flask_session.Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        return flask.render_template("index.html")
    else:
        return flask.render_template("index.html")
       
