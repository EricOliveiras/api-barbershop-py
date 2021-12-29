from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import DateTime

from database.config.connect import Base


class Service(Base):

  __tablename__ = "service"

  id = Column(Integer, primary_key=True ,autoincrement=True)
  price = Column(Float, nullable=False)
  barber_id = Column(Integer, ForeignKey("barber.id"), nullable=False)
  client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
  created_at = Column(DateTime, default=now())
  updated_at = Column(DateTime, default=now(), onupdate=now())
