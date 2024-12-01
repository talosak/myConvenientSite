# MyConvenientSite
#### Video Demo: PLACEHOLDER
#### Description: MyConvenientSite (MCS) is a simple web application intended to do some easy, everyday things. It's purpose is to be a simple yet convenient resource. A hub of sorts that performs actions which everyone does fairly often.

## Built With
* [Bootstrap](https://getbootstrap.com/)
* [Flask](https://flask.palletsprojects.com/en/stable/)

## Getting Started
1. Download [python and pip](https://www.python.org/)
2. Download [VSCode](https://code.visualstudio.com/)
3. Download [Git](https://git-scm.com/)
4. Open VSCode and download the python extension
5. Create a terminal using the Git Bash
6. Clone the Github repository
    ```bash
    git clone https://github.com/talosak/myConvenientSite.git
    ```
7. Install flask and flask-session
    ```bash
    python -m pip install flask
    python -m pip install flask
    ```
8. Run the web application
    ```bash 
    python -m flask run
    ```

# Documentation
### This is the main parte of the README where i go into detail about every file and feature
## Introduction
The idea for MCS came about because i wanted to use everything i learned during the entire course in my final project. To reinforce all the tools i gathered from CS50, that being:
* Python (week 6 and weeks 0-5 as a lead up to it)
* SQLite (week 7)
* HTML, Bootstrap, Javascript, CSS (week 8)
* Flask (week 9)

The project was heavily inspired by the final task of problem set 9, "Finance". It was my second favorite assignment from the course (my favorite was week 7's Fiftyville).

I made MCS **without** using the CS50 codespace or library. It was still in VSCode, but not in the codespace. I wanted to take all the training wheels off, to feel like i have succeded and do not need them anymore. Thanks to this i learned a lot from the experience. I am now very comfortable with git and can connect a flask webapp to a database on my own.

It took me about three weeks to complete the final project from start to finish.

## Design
Most of the styling i did with bootstrap. However i also created many of my own styles. Most of them are just recolors of the bootstrap classes or font size changes.

My most used class of my own creation is "btn-pink", which is a custom style for the bootstrap "btn" class.

I also made dark versions for the three types of flash alerts i used (success, failure, info)

## Features
I will discuss each individual feature in more detail later, but they were intended to be simple, everyday things that most people do. They were all pretty simple to make, comparable to the different features of week 9's "Finance".

The features are:
* Calculator - a calculator with addition, multiplication, subtraction and division
* CPS - a test of how fast a person can click their mouse
* Date - displays the current date, time and day of the week
* Home - the homepage, greets the user
* Login - allows the user to log into an existing account
* Logout - allows the user to log out
* Register - allows the user to create an account
* Reminders - allows the user to create and delete reminders
* Rename - allows the user to rename their account
* RNG - generates a random number from a specified range

## Database
The database is stored in the file "myConvenientSite.db". It is used to hold all the user data.

The database consists of three tables:
* users
* reminders
* cps_high_scores

The "users" table is used to hold the basic user information. It achieves this through three columns:
* id - the user's id number
* username - the user's username
* passwordHash - the user's hashed password

.schema for "users":
```sqlite3 
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, passwordHash TEXT NOT NULL);
```

The "reminders" table holds information about the reminders from the "/reminders" route. It uses four columns:
* reminder_id - a given reminder's id number
* user_id - the id of the user who has the reminder
* content - the reminder's content
* creationTime - the time at which the reminder was created

.schema for "reminders":
```sqlite3
CREATE TABLE reminders (reminder_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER NOT NULL, content TEXT NOT NULL, creationTime TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id));
```

The "cps_high_scores" table holds information about the highscores from the "/cps" route. It uses three columns:
* highscore_id - a given highscore's id number
* user_id - the id of the user who has the highscore
* highscore - the highscore itself

.schema for "cps_high_scores"
```sqlite3
CREATE TABLE cps_high_scores (highscore_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, user_id INTEGER NOT NULL, highscore INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id));
```

## Layout
It's main purpose is to create the navbar and flash messages with the "flask.flash()" function. Contained in the "layout.html" file.

Every template extends the "layout.html" file.

The navbar is heavily inspired by the one from "Finance", overall it is very similar to it's inspiration. The main differences are that it is slightly bigger, and the brand and logo is different. It makes heavy use of bootstrap for it's formatting. 

The logo is my original idea. It's just supposed to be the ":3" emoticon. With pink and purple as the colors, because i thought it looked neat.

Every item on the navbar is a link to something. The logo is a link to the homepage, next to the logo are links to the features, and all the way on the right is the link to the "/logout" route.

If the user is not logged in then the navbar changes to have links to "/login" and "/register" instead of all the features. This is achieved by checking if the user has a session user_id with a Jinja "if" statement.

It's secondary use is flashing messages with the "flask.flash()" python function.

There are three self explanatory types of messages:
* flash-success - informs of something good
* flash-failure - informs of something bad
* flash-info - informs of something neither good or bad

The messages have a button that allows the user to close them

## Register
Allows the user to create an account. It's route is "/register". It's template is "register.html"

There are several requirements to creating an account:
* The user is required to fill out and submit a "POST" form with their username, password and a confirmation of their password
* The username cannot be longer than 12 characters
* The password and confirmation must be the same 
* The username must not be already taken by another user. 

If any of these requirements are not fulfilled a flash-failure message is displayed and the user must try again.

If the user successfully creates an account they are automatically assigned a user id. Their id, username and hashed password (hashed with the "generate_password_hash()" function) is saved to the "users" table of the database. Afterwards their session user_id is set to their id from the database.

The user is then redirected to Index.

## Log in
Allows the user to log into an existing account. It's route is "/login". It's template is "login.html"

If a user tries to access any route that requires being logged in without being logged in (i.e. having a session user_id), they will be automatically redirected here.

There are several requirements to creating an account:
* The user must fill out and submit a "POST" form with their username and password
* The username must already exist
* The password must be correct - checked by "check_password_hash()"

If any of these requirements are not fulfilled a flash-failure message is displayed and the user must try again.

If the user successfully logs into an account their session user_id is set to their id from the database and they are redirected to Index.

## Index
A simple page with only the text: "Hello, {{username}}", "Glad to see you". It's route is "/". It's template is "index.html". Requires being logged in.

It is intended to greet the user upon logging in. Whenever the user successfully submits a "POST" request they are redirected here most of the time. 

This page can also be accessed by clicking on the MCS logo.

## Log Out
Allows the user to log out of an account. It's route is "/logout". It does not have a template. Requires being logged in.

Clears the user's information from the session with "flask.session.clear()".

Redirects to Index, which then redirects to Log in.

## Calculator
A basic calculator. It's route is "/calculator". It's template is "calculator.html". Requires being logged in.

It has a script in the file "calculatorScript.js". It checks which button was pressed and displays them on the display. It can clear when pressing the "c" button and performs the action when the "=" button is pressed, using the "math.eval()" function in Javascript

The calculator can perform the four basic arithmetic functions, those being:
* addition
* subtraction
* multiplication
* division

It also supports non-integer and negative numbers.

## CPS
Measures how quickly a user can click their mouse. It's route is "/cps". It's templates are "cps.html" and "cpsResults.html". Requires being logged in.

This is the most complicated feature. It uses every language i know.

When the method is "GET"  the "cps.html" template is rendered with a button to begin the cps test, a display of time remaining, the amount of clicks during the current test and the user's all time most clicks in a test (highscore).

The highscore is taken from the "cps_high_scores" table from the database and displayed with Jinja.

When the button is pressed a ten second timer begins and the amount of times the button is clicked by the user begins being tracked inside the "cpsScript.js" file.

When the timer is up a "POST" form is submitted, with the number of clicks saved in a hidden element.

If the amount of clicks is bigger than the user's highscore then it is set as the new high score, overwriting the previous one.

If the user does not have a highscore then it is inserted into the database.

Then the "cpsResults.html" is rendered. It displays the amount of clicks during the test, the click speed (in clicks per second). It also shows the highest amount of clicks the user ever got, as well as their speed in that test.

## Date
Displays the current date, time and day of the week. It's route is "/dateandtime". It's template is "dateandtime.html". Requires being logged in.

It gets the date and time from the datetime python library and displays via Jinja.

Only updates on page refresh.

## Reminders
Allows the user to create and delete little reminders. It's routes are "/reminders" and "/reminderCreate". It's templates are "reminders.html" and reminderCreate.html". Requires being logged in.

It is the only feature with two routes.

Upon a "GET" request to "/reminders" the "reminders.html" template is rendered.

All the reminders are generated with a Jinja "for" loop.

Every delete button is of type "submit" and has a value equal to the given reminder's reminder_id. That way when a delete button is pressed, the id of the reminder that should be deleted can be read directly from the clicked button's value.

There is also a button to add reminders, this is just a link that redirects the user to the "/reminderCreate" route.

Upon a "GET" request to "/reminderCreate" the "reminderCreate.html" template is rendered. The user should fill type in the text input field what they want the content of their reminder to be. It **can** be empty, but **cannot** be longer than 45 characters.

Upon a successful submit, a new reminder is inserted into the "reminders" table of the database with a reminder_id, a user_id, the content provided by the user as well as the date and time of creation obtained using the datetime python library.

## Rename
Allows the user to change their own username. It's route is "/rename". It's template is "rename.html" Requires being logged in.

The user is expected to fill out a "POST" form, very similar to the one in Login. However here instead of inputting their current username, they should input the new username that they want.

The requirements for a new username are a combination of the ones in Login and Register:
* The username cannot be longer than 12 characters
* The username must not be already taken by them or another user
* The password must be correct

Here the password is checked with the user's id, unlike Login where it is checked with their username.

Upon a successful rename the new username replaces the old one in the "users" table and the user is redirected to Index.

## RNG
Generates a random number within a specified range. It's route is "/rng". It's templates are "rng.html" and "rng-ed.html". Requires being logged in.

Upon a "GET" request the user is expected to fill out a "POST" form with a minimal and maximal number that they'd like to be in the random generation pool.

Both numbers have to be positive integers. Non numeric, negative or decimal values are not supported and will return a failure message. 

Upon a successful generation the "rng-ed.html" template is rendered, showing the result.

## Licence
MIT License

Copyright (c) 2024 Igor Selma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
