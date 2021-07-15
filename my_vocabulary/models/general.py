import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean, DateTime, Enum, Integer, String


Base = declarative_base()
metadata = Base.metadata


class Language(enum.Enum):
    english = 0
    french = 1
    german = 2


class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)

    text = Column(String, nullable=False)
    language = Column(Enum(Language), nullable=False)
    audio_file = Column(String)
    image_file = Column(String)
    notes = relationship("Note", back_populates="entry")


class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)

    text = Column(String, nullable=False)
    entry_id = Column(Integer, ForeignKey("entry.id"))
    entry = relationship("Entry", back_populates="notes", lazy="joined")
