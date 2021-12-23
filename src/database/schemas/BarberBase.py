from pydantic import BaseModel
from typing import Optional

class Barber_Base(BaseModel):
  name: str
  document: str
  phone: Optional[str] = None

  class Config:
    orm_mode = True


class Barber_update(BaseModel):
  name: Optional[str] = None
  document: Optional[str] = None
  phone: Optional[str] = None

  class Config:
    orm_mode = True