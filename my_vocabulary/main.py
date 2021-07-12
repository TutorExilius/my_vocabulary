import configparser

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.general import Language, Vocabulary

alembic_config = configparser.ConfigParser()
alembic_config.read("alembic.ini")
database_url = alembic_config["alembic"]["sqlalchemy.url"]

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    voc_1 = Vocabulary(word="test", language=Language.english)
    session.add(voc_1)
    session.commit()


if __name__ == "__main__":
    main()
