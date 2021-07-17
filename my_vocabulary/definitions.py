import datetime

from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer


class BaseExtension:
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
