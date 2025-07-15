from database import SessionLocal
from query_helpers import *

db = SessionLocal()

movies = get_movies(db, limit=5)

for movie in movies:
    print(f"Id: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")

db.close()