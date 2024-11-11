import os
import flask
import flask_session

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"