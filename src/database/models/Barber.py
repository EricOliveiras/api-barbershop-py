from sqlalchemy import Column, Integer, String

from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import DateTime

from src.database.config.connect import Base

class Barber(Base):
  __tablename__ = "barber"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  document = Column(String(20), nullable=False, unique=True)
  phone = Column(String(20), nullable=True)
  create_at = Column(DateTime, default=now())
  update_at = Column(DateTime, default=now())
