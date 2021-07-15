import configparser
from datetime import datetime as dt

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.general import Language, Entry, Note

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


def main():
    pass


if __name__ == "__main__":
    main()
