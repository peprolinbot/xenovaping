from sqlalchemy import Column, BigInteger, String, Boolean
from sqlalchemy.types import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Card(Base):
    __tablename__ = "cards"
    number = Column(BigInteger, primary_key=True)
    email = Column(String)
    notified = Column(Boolean)
