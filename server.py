"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage.
        Falmingos, Pink, Black 1950's Miami Kitchen.
        Index page that shows options to look at with simple menu
    """

    return render_template('homepage.html')

@app.route('/movies')
def movies_list_page():
    """Movie List Page. Can Organize Movie info in a table that you can Organize by title or release date
        WILL NEED ROUTES FOR AJAX
    """

    return render_template('movies-list.html')



@app.route('/movie-detail/<int:movie_id>')
def movie_detail_page():
    """Individual Movie Info Page."""
    ## CHANGE TO MOVIE THINGS
    # melon = model.Melon.get_by_id(id)
    # print melon
    return render_template("movie-detail.html")
    #will need to pass movie query information through jinja into template


@app.route('/user-list')
def user_list_page():
    """List of all users in a pretty pretty table."""

    users = User.query.all()
    return render_template("user-list.html", users=users)


@app.route('/user-profile/<int:user_id>')
def user_detail_page():
    """List of all users in a pretty pretty table."""

    return render_template("user-detail.html")


@app.route('/loggin')
def loggin_page():
    """List of all users in a pretty pretty table.
        MAY BE MODAL WITH AJAX
    """

    return render_template("loggin.html")


@app.route('/logout')
def loggin_page():
    """List of all users in a pretty pretty table.
        MAY BE MODAL WITH AJAX
    """

    return render_template("logout.html")


@app.route('/registration')
def register_page():
    """Register new users in the database.
        check that email is not already in database
        and either add to database or ask to loggin if email exists.
    """

    return render_template("register.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()