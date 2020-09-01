from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from core.config import settings

SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost:5432"

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)