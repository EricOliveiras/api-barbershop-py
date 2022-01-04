from pydantic import BaseModel
from typing import Optional


class Payment_Base(BaseModel):
  barber_id: int

  class Config:
    orm_mode = True


class Payment_Update(BaseModel):
  barber_id: Optional[int]

  class Config:
    orm_mode = True