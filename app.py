import os
import flask
import flask_session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = flask.Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
flask_session.Session(app)

def connectDB():
    db = sqlite3.connect("myConvenientSite.db")
    db.row_factory = sqlite3.Row
    return db

@app.route("/")
def index():
    if flask.session.get("user_id") is None:
            return flask.redirect("/login")
    db = connectDB()
    username = db.execute("SELECT username FROM users WHERE id = ?", (flask.session["user_id"],)).fetchone()["username"]
    db.close()
    return flask.render_template("index.html", username=username)
    
@app.route("/login", methods=["GET", "POST"])
def login():
     if flask.request.method == "POST":
        if not flask.request.form.get("username") or not flask.request.form.get("password"):
            flask.flash("Username or password missing", "flash-failure")
            return flask.redirect("/login")
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        db = connectDB()
        if len(db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()) == 0:
             db.close()
             flask.flash("There is no user with that name", "flash-failure")
             return flask.redirect("/login")
        if not check_password_hash(db.execute("SELECT passwordHash FROM users WHERE username = ?", (username,)).fetchone()["passwordHash"], password):
            db.close()
            flask.flash("Incorrect password", "flash-failure")
            return flask.redirect("/login")
        flask.session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()["id"]
        return flask.redirect("/")
     else:
          return flask.render_template("login.html")
     
@app.route("/logout")
def logout():
    if flask.session.get("user_id") is None:
            return flask.redirect("/login")
    flask.session.clear()
    return flask.redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "POST":
        if not flask.request.form.get("username") or not flask.request.form.get("password") or not flask.request.form.get("confirmation"):
             flask.flash("Username, password or confirmation missing", "flash-failure")
             return flask.redirect("/register")
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        confirmation = flask.request.form.get("confirmation")
        if password != confirmation:
             flask.flash("Password doesn't match confirmation", "flash-failure")
             return flask.redirect("/register")
        if len(username) > 12:
             flask.flash("Username can't be longer than 12 letters", "flash-failure")
             return flask.redirect("/register")
        db = connectDB()
        if len(db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()) != 0:
             db.close()
             flask.flash("Username is already taken", "flash-failure")
             return flask.redirect("/register")
        db.execute("INSERT INTO users (username, passwordHash) VALUES (?, ?)", (username, generate_password_hash(password)))
        db.commit()
        flask.session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()["id"]
        db.close()
        return flask.redirect("/")
    else:
        return flask.render_template("register.html")
    