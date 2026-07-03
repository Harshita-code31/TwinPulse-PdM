from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config.settings import get_settings
from app.database.models import Base

settings = get_settings()


def create_database_engine():
    """
    Create SQLAlchemy engine.
    """
    return create_engine(
        settings.database_url,
        echo=False,
        pool_pre_ping=True,
    )


def create_session_factory():
    """
    Create SQLAlchemy session factory.
    """
    engine = create_database_engine()

    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )


def get_database_session() -> Generator[Session, None, None]:
    """
    Return a database session.
    """

    session_factory = create_session_factory()

    db = session_factory()

    try:
        yield db

    finally:
        db.close()


get_db = get_database_session


def initialize_database():
    """
    Create all database tables.
    """

    engine = create_database_engine()

    Base.metadata.create_all(bind=engine)