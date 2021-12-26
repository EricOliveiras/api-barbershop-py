from pydantic import BaseModel
from typing import Optional


class Client_Base(BaseModel):
  name: str
  email: str
  phone: Optional[str] = None

  class config:
    orm_mode = True


class Client_Update(BaseModel):
  name: Optional[str] = None
  email: Optional[str] = None
  phone: Optional[str] = None

  class config:
    orm_mode = True