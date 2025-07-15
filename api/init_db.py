from database import Base, engine
from models import Movie, Rating, Tag, Link  # adapte selon ton projet

Base.metadata.drop_all(bind=engine)  # si tu veux repartir de zéro
Base.metadata.create_all(bind=engine)
print("Base de données initialisée.")
