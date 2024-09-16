from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine, SessionLocal = None, None

try:
    DATABASE_URL = "localhost:3000"
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    print(f"An error occurred: {str(e)}")
