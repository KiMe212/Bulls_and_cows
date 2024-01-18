from database import Base
from sqlalchemy import Column, Integer, String


class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    attempts = Column(Integer)
    number = Column(String, nullable=False)
