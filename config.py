import os

import busGal_api as busgal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from contextlib import contextmanager

import database

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
# Set up database
Session = sessionmaker()
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
database.Base.metadata.create_all(bind=engine)
Session.configure(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
# ---------------

TPGAL_EMAIL = os.environ.get('TPGAL_EMAIL')
TPGAL_PASSWORD = os.environ.get('TPGAL_PASSWORD')
# Login to TPGAL
account = busgal.Account(email=TPGAL_EMAIL, password=TPGAL_PASSWORD)
# --------------

CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL', 86400))

APPRISE_EMAIL_URL = os.environ.get('APPRISE_EMAIL_URL')
