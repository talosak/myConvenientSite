import os
import flask
import flask_session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

app = flask.Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
flask_session.Session(app)

def connectDB():
    db = sqlite3.connect("myConvenientSite.db")
    db.row_factory = sqlite3.Row
    return db

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        db = connectDB()
        db.execute("INSERT INTO example (example1, example2) VALUES (?, ?)", (20, 'success'))
        db.commit()
        db.close()
        flask.flash("Example successful", "flash-success")
        return flask.render_template("index.html")
    else:
        return flask.render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "POST":
        return flask.render_template("register.html")
    else:
        return flask.render_template("register.html")