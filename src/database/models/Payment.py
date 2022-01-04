from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import Float

from src.database.config.connect import Base

class Payment(Base):
  __tablename__ = "payment"

  id = Column(Integer, primary_key=True, autoincrement=True)
  barber_id = Column(Integer, ForeignKey("barber.id"), nullable=False)
  total_payment = Column(Float, nullable=False)
  created_at = Column(DateTime, default=now())
  updated_at = Column(DateTime, default=now(), onupdate=now())

  services = relationship("Service", back_populates="payment")
  barber = relationship("Barber", back_populates="payment")
