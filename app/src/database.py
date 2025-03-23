import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

###
# Database Configuration
###

SQLALCHEMY_DATABASE_URL = "postgresql://rin:fastapi@localhost:5432/yt-clone"
connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()