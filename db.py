from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy

# create db object
db=SQLAlchemy()

'''
@contextmanager
def session_scope(db):
    session = db.session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
'''