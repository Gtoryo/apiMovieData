from database import SessionLocal
from query_helpers import *

db = SessionLocal()

movies = get_movies(db, limit=5)

for movie in movies:
    print(f"Id: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")


ratings = get_ratings(db, limit=5, min_rating=3.0)

for rating in ratings:
    print(f"IdUser: {rating.userId}, IdMovie: {rating.movieId}, Note: {rating.rating}")

db.close()