import enum
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean, DateTime, Enum, Integer, String

from my_vocabulary.definitions import BaseExtension


Base = declarative_base()
metadata = Base.metadata


class Language(enum.Enum):
    ENGLISH = 0
    FRENCH = 1
    GERMAN = 2


class CardBox(Base, BaseExtension):
    __tablename__ = "cardbox"

    # 1 to many relation between CardBox(parent) -> Tray(child)
    trays = relationship("Tray", back_populates="cardbox", cascade="all, delete-orphan")


class Tray(Base, BaseExtension):
    __tablename__ = "tray"

    poll_interval = Column(Integer, nullable=False)

    # 1 to many relation between Tray(parent) -> FlashCard(child)
    flashcards = relationship("FlashCard", back_populates="tray")

    # 1 to many relation between CardBox(parent) -> Tray(child)
    cardbox_id = Column(Integer, ForeignKey("cardbox.id"))
    cardbox = relationship("CardBox", back_populates="trays")


class FlashCard(Base, BaseExtension):
    __tablename__ = "flashcard"

    image_file = Column(String)
    last_poll_date = Column(DateTime)
    count_right = Column(Integer, nullable=False, default=0)
    count_wrong = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, default=True)
    adult_only = Column(Boolean, default=False)

    # 1 to many relation between FlashCard(parent) -> FlashCardPage(child)
    pages = relationship("FlashCardPage", back_populates="flashcard", cascade="all")

    # 1 to many relation between Tray(parent) -> FlashCard(child)
    tray_id = Column(Integer, ForeignKey("tray.id"), nullable=False)
    tray = relationship("Tray", back_populates="flashcards")

    def __init__(self, tray):
        self.tray = tray
        self.last_poll_date = datetime.datetime.utcnow()


class FlashCardPage(Base, BaseExtension):
    __tablename__ = "flashcardpage"

    # 1 to 1 relation between FlashCardPage(parent) -> Entry(child)
    entry = relationship(
        "Entry",
        back_populates="flashcardpage",
        uselist=False,
        cascade="all, delete-orphan",
    )

    # 1 to many relation between FlashCard(parent) -> FlashCardPage(child)
    flashcard_id = Column(Integer, ForeignKey("flashcard.id"), nullable=False)
    flashcard = relationship("FlashCard", back_populates="pages", cascade="all, delete")


class Entry(Base, BaseExtension):
    __tablename__ = "entry"

    text = Column(String, nullable=False)
    language = Column(Enum(Language), nullable=False)
    audio_file = Column(String)
    is_definition = Column(Boolean, default=False)

    # 1 to many relation between Entry(parent) -> Note(child)
    notes = relationship("Note", back_populates="entry", cascade="all, delete-orphan")

    # 1 to 1 relation between FlashCardPage(parent) -> Entry(child)
    flashcardpage_id = Column(Integer, ForeignKey("flashcardpage.id"), nullable=False)
    flashcardpage = relationship("FlashCardPage", back_populates="entry", cascade="all")


class Note(Base, BaseExtension):
    __tablename__ = "note"

    text = Column(String, nullable=False)

    # 1 to many relation between Entry(parent) -> Note(child)
    entry_id = Column(Integer, ForeignKey("entry.id"))
    entry = relationship("Entry", back_populates="notes")
