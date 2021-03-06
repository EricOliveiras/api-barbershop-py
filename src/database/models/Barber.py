from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from src.database.config.connect import Base


class Barber(Base):
  __tablename__ = "barber"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(250), nullable=False)
  document = Column(String(20), nullable=False, unique=True)
  phone = Column(String(20), nullable=True)
  created_at = Column(DateTime, default=now())
  updated_at = Column(DateTime, default=now(), onupdate=now())

  services = relationship("Service", back_populates="barber")
  payment = relationship("Payment", back_populates="barber")
