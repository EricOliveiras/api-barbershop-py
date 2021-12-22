from sqlalchemy.orm import Session

from src.database.models.Barber import Barber
from src.database.schemas.BarberBase import BarberBase

class BarberController:
  def __init__(self, db: Session):
    self.db = db

  def create_barber(self, BarberBase: BarberBase):

    barber_exists = self.db.query(Barber).filter(Barber.document == BarberBase.document).first()

    if not barber_exists:
      db_barber = Barber(
        name = BarberBase.name,
        document = BarberBase.document,
        phone = BarberBase.phone
      )

      self.db.add(db_barber)
      self.db.commit()
      self.db.refresh(db_barber)

      return db_barber

    else:
      return f'Barber already exists'


  def get_all_barbers(self):

    all_barbers = self.db.query(Barber).all()

    if all_barbers.__len__() == 0:
      return f'No barbers found'
    else:
      return all_barbers


  def get_barber_by_id(self, id: int):

    get_barber = self.db.query(Barber).filter(Barber.id == id).first()

    if not get_barber:
      return f'Barber not found'

    return get_barber

    