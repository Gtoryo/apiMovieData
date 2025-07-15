from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# Tester la récupération de quelques films

movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"Id: {movie.movieId}, Titre : {movie.title}, Genre: {movie.genres}")

# Récupération de films par genre(Action)

action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(5).all()

for action_movie in action_movies:
    print(f"Id: {action_movie.movieId}, Titre : {action_movie.title}, Genre: {action_movie.genres}")


# Récupération des notes des films

ratings = db.query(Rating).limit(5).all()

for rating in ratings:
    print(f"Id: {rating.movieId}, rating: {rating.rating}, Timestamp: {rating.timestamp}")

# Récupération des films qui ont une note > 4

hight_rated_movies = (db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
)

for title, rating in hight_rated_movies:
    print(f"Title: {title}, Rating: {rating}")

# Récupération des tags associés aux films

tags = db.query(Tag).limit(5).all()

for tag in tags:
    print(f"Id: {tag.movieId}, Tag: {tag.tag}")

# # Récupération des liens associés aux films

links = db.query(Link).limit(5).all()

for link in links:
    print(f"Id: {link.movieId}, Tag: {link.imdbId}")

db.close()