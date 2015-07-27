"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""
    with open('/seed_data/u.user', 'r') as user_data:
        for line in user_data:
            row = line.split('|')

            user_id = row[0]
            age = row[1]
            email = None
            password = None
            zipcode = row[4]
            user_inserted = model.User(user_id, email, password, age, zipcode)
            db.session.add(user_inserted)
        db.session.commit()

        

def load_movies():
    """Load movies from u.item into database."""
    with open('/seed_data/u.item', 'r') as movie_data:
        for line in movie_data:
            row = line.split('|')


def load_ratings():
    """Load ratings from u.data into database."""
    with open('u.data', 'r') as rating_data:

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()
