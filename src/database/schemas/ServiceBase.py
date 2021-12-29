from pydantic import BaseModel
from typing import Optional


class Service_Base(BaseModel):
  price: float
  barber_id: int
  client_id: int

  class Config:
    orm_mode = True


class Service_Update(BaseModel):
  price: Optional[float] = None
  barber_id: Optional[int] = None
  client_id: Optional[int] = None

  class Config:
    orm_mode = True