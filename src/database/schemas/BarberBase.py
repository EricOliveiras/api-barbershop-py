from pydantic import BaseModel
from typing import Optional

class BarberBase(BaseModel):
  name: str
  document: str
  phone: Optional[str] = None

  class Config:
    orm_mode = True