from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from src.database.config.connect import Base


class Service(Base):

  __tablename__ = "service"

  id = Column(Integer, primary_key=True ,autoincrement=True)
  price = Column(Float, nullable=False)
  barber_id = Column(Integer, ForeignKey("barber.id"), nullable=False)
  client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
  payment_id = Column(Integer, ForeignKey("payment.id"), nullable=False)
  created_at = Column(DateTime, default=now())
  updated_at = Column(DateTime, default=now(), onupdate=now())

  barber = relationship("Barber", back_populates="services")
  client = relationship("Client", back_populates="services")
  payment = relationship("Payment", foreign_keys=[payment_id], back_populates="services") 