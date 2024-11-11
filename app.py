import os
import flask
import flask_session
from werkzeug.security import check_password_hash, generate_password_hash

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")
