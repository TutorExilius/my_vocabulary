import sys
import configparser
from datetime import datetime as dt
from my_vocabulary.flashcard_dialog import FlashCardDialog

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from PyQt5.QtWidgets import QApplication

from models.general import (
    Entry,
    Note,
    Tray,
    FlashCard,
    FlashCardPage,
    CardBox,
)

alembic_config = configparser.ConfigParser()
alembic_config.read("../alembic.ini")
database_url = alembic_config["alembic"]["sqlalchemy.url"].replace(
    "sqlite:///", "sqlite:///../"
)

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

lang_1 = "Deutsch"
lang_2 = "Französisch"

def main_3():
    entry = session.query(Entry).get(1)
    del entry.notes[-1]

    session.commit()


def main_2():
    entry = session.query(Entry).get(1)
    session.delete(entry)
    session.commit()


def main():
    entry_1 = Entry(text="test", language=lang_1)

    note_1 = Note(text="this is a example")
    note_2 = Note(text="this is another example")

    entry_1.notes = [note_1, note_2]

    session.add(entry_1)
    session.add(note_1)
    session.add(note_2)

    session.commit()

    if True:
        print("test.....")


def create_notes(entry):
    note_1 = Note(text="this is a example")
    note_2 = Note(text="this is another example")
    entry.notes = [note_1, note_2]

    session.add(note_1)
    session.add(note_2)

example_translations = {
    lang_1: ["Test", "hallo", "Guten Tag", "Guten Abend", "die Frau", "der Mann", "der Junge", "das Mädchen", "der Ball"],
    lang_2: ["test", "salut", "Bonjour", "Bonsoir", "la femme", "l'homme (m.)", "le garçon", "la fille", "le balon"]
}

entry_counter = 0
word_cnt = 0
def create_entry(flashcardpage):
    global entry_counter, word_cnt

    if entry_counter % 2 == 0:
        entry = Entry(
            text=example_translations[lang_1][word_cnt],
            language=lang_1,
            flashcardpage=flashcardpage
        )
    else:
        entry = Entry(
            text=example_translations[lang_2][word_cnt],
            language=lang_2,
            flashcardpage=flashcardpage
        )
        word_cnt += 1

    session.add(entry)
    entry_counter += 1
    return entry


def create_cardbox():
    cardbox = CardBox(language_1=lang_1, language_2=lang_2)

    tray_1 = Tray(poll_interval=1)
    tray_2 = Tray(poll_interval=3)
    tray_3 = Tray(poll_interval=7)

    cardbox.trays = [tray_1, tray_2, tray_3]

    session.add(cardbox)
    return cardbox


def create_flashcards(cardbox):
    for tray in cardbox.trays:
        for _ in range(3):
            flashcard = FlashCard(tray=tray)

            flashcardpage_1 = FlashCardPage()
            flashcardpage_1.entry = create_entry(flashcardpage_1)
            create_notes(flashcardpage_1.entry)

            session.add(flashcardpage_1)

            flashcardpage_2 = FlashCardPage()
            flashcardpage_2.entry = create_entry(flashcardpage_2)
            create_notes(flashcardpage_2.entry)

            session.add(flashcardpage_2)

            flashcard.pages = [flashcardpage_1, flashcardpage_2]

            tray.add_flashcard(flashcard)
            session.add(flashcard)



if __name__ == "__main__":
    if 0:
        app = QApplication([])
        window = FlashCardDialog()
        window.show()
        sys.exit(app.exec_())
    else:
        cardbox = create_cardbox()
        create_flashcards(cardbox)
        session.commit()
        exit()

    cardbox = session.query(CardBox).get(1)

    for tray in cardbox.trays:
        for flashcard in tray.flashcards:
            session.delete(flashcard)

        session.delete(tray)
        session.commit()
        exit()
        for flashcard in tray.flashcards:
            session.delete(flashcard.pages[0])
            session.commit()

    session.delete(cardbox)
    session.commit()
