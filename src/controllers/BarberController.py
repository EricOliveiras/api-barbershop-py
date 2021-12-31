from sqlalchemy.orm import Session

from src.database.models.Barber import Barber
from src.database.schemas.BarberBase import Barber_Base, Barber_update
from src.database.models.Service import Service

class BarberController:
  def __init__(self, db: Session):
    self.db = db

  def create_barber(self, Barber_Base: Barber_Base):

    barber_exists = self.db.query(Barber).filter(Barber.document == Barber_Base.document).first()

    if not barber_exists:
      new_barber = Barber(
        name = Barber_Base.name,
        document = Barber_Base.document,
        phone = Barber_Base.phone
      )

      self.db.add(new_barber)
      self.db.commit()
      self.db.refresh(new_barber)

      return new_barber

    else:
      return f'Barber already exists'


  def get_all_barbers(self):

    all_barbers = self.db.query(Barber).all()

    if all_barbers.__len__() == 0:
      return f'No barbers found'
    else:
      return [{
        'id': barber.id,
        'name': barber.name,
        'document': barber.document,
        'phone': barber.phone,
        'created_at': barber.created_at,
        'updated_at': barber.updated_at,
        'services': [{
          'id': service.id,
          'price': service.price,
          'client': service.client.name,
          'created_at': service.created_at,
          'updated_at': service.updated_at
        } for service in barber.services] 
      } for barber in all_barbers
    ]


  def get_barber_by_id(self, id: int):

    get_barber = self.db.query(Barber).filter(Barber.id == id).first()

    if not get_barber:
      return f'Barber not found'

    return {
      'id': get_barber.id,
      'name': get_barber.name,
      'document': get_barber.document,
      'phone': get_barber.phone,
      'created_at': get_barber.created_at,
      'updated_at': get_barber.updated_at,
      'services': [{
        'id': service.id,
        'price': service.price,
        'client': service.client.name,
        'created_at': service.created_at,
        'updated_at': service.updated_at
      } for service in get_barber.services]
    }

    
  def get_barber_by_document(self, document: str):

    get_barber = self.db.query(Barber).filter(Barber.document == document).first()

    if not get_barber:
      return f'Barber not found'

    return get_barber


  def update_barber(self, id: int, Barber_update: Barber_update):

    barber = self.db.query(Barber).filter(Barber.id == id).first()

    if not barber:
      return f'Barber not found'

    for key, value in Barber_update.__dict__.items():
      setattr(barber, key, value) if value else None

    self.db.commit()
    self.db.refresh(barber)

    return barber


  def delete_barber(self, id: int):
      
    barber = self.db.query(Barber).filter(Barber.id == id).first()

    if not barber:
      return f'Barber not found'

    self.db.delete(barber)
    self.db.commit()

    return f'Barber deleted'