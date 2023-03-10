from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///./" "app.db", connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    It creates a database session, yields it to the caller, and then closes the session when the caller is done
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
