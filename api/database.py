"Configuration de la connexion à la base de données"

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de la base de données SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

# Création de l'engine (connexion à la base)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de tous les modèles
Base = declarative_base()

# Vérification de la connexion (optionnelle)
# if __name__ == "__main__":
#     try:
#         with engine.connect() as conn:
#             print("Connexion à la base réussie")
#     except Exception as e:
#         print(f"Erreur de connexion à la base de données : {e}")
