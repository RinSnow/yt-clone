"""This file contains the database configuration and the database session."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from .config import get_settings
###
# Database Configuration
###

db_settings = get_settings()
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_settings.db_user}:{db_settings.db_pass}@{db_settings.db_host}:5432/yt-clone"
print(db_settings.url_test)
connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()