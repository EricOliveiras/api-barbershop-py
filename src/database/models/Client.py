from sqlalchemy import Column, Integer, String

from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import DateTime

from src.database.config.connect import Base


class Client(Base):
  __tablename__ = "client"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(250), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  phone = Column(String(20), nullable=True)
  created_at = Column(DateTime, default=now())
  updated_at = Column(DateTime, default=now(), onupdate=now())