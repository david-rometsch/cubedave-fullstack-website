"""
database.py — Database engine, session factory, and dependency injection.

Centralises all SQLAlchemy setup so main.py stays focused on route logic.
"""

from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from models import Base

# SQLite database engine
engine = create_engine("sqlite:///database.db")

# Session factory — autocommit disabled so commits are explicit
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables defined in models if they don't exist yet
Base.metadata.create_all(engine)

# Migrate existing databases: add image2/image3 columns if not present
with engine.connect() as conn:
    for col in ("image2", "image3"):
        try:
            conn.execute(text(f"ALTER TABLE products ADD COLUMN {col} TEXT"))
            conn.commit()
        except Exception:
            pass  # column already exists


@contextmanager
def get_session():
    """Context manager for database sessions used in startup/seeding code."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def get_db():
    """Dependency-injected session for FastAPI route handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
