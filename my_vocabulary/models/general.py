import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.types import Enum

Base = declarative_base()
metadata = Base.metadata

class Language(enum.Enum):
    english = 0
    french = 1
    german = 2

class Vocabulary(Base):
    __tablename__ = 'vocabulary'

    id = Column(INTEGER(11), primary_key=True)
    word = Column(String)
    language = Column(Enum(Language), default=Language.english)



