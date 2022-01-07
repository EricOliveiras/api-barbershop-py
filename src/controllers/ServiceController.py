from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text

from src.database.models.Service import Service
from src.database.models.Barber import Barber
from src.database.models.Client import Client
from src.database.schemas.ServiceBase import Service_Base, Service_Update


class ServiceController:
  def __init__(self, db: Session):
    self.db = db

  def create_service(self, Service_Base: Service_Base): 

    barber_exist = self.db.query(Barber).filter(Barber.id == Service_Base.barber_id).first()
    client_exist = self.db.query(Client).filter(Client.id == Service_Base.client_id).first()

    if not barber_exist or not client_exist:
      return 'Barber or Client not found'

    new_service = Service(
      price = Service_Base.price,
      barber_id = Service_Base.barber_id,
      client_id = Service_Base.client_id
    )

    self.db.add(new_service)
    self.db.commit()  
    self.db.refresh(new_service)

    return new_service

  def get_all_services(self):

    get_services = self.db.query(Service).all()

    if get_services.__len__ == 0:
      return 'No services found'
    
    format_services = [{
      'id': service.id,
      'price': service.price,
      'barber': service.barber.name,
      'client': service.client.name,
      'created_at': service.created_at,
      'updated_at': service.updated_at
      } for service in get_services
    ]

    return format_services


  def get_service_by_id(self, id: int):
      
    get_service = self.db.query(Service).filter(Service.id == id).first()

    if not get_service:
      return 'Service not found'

    format_service = {
      'id': get_service.id,
      'price': get_service.price,
      'barber': get_service.barber.name,
      'client': get_service.client.name,
      'created_at': get_service.created_at,
      'updated_at': get_service.updated_at
    }

    return format_service


  def get_service_by_date(self, date: str):

    get_date = date.split('-')
    day = get_date[0]
    month = get_date[1]
    year = get_date[2]

    format_date = f'{year}-{month}-{day}'
 
    get_services = self.db.query(Service).filter(text(f"date(created_at) = '{format_date}' ")).all()

    if get_services.__len__ == 0:
      return 'No services found'

    format_services = [{
      'id': service.id,
      'price': service.price,
      'barber': service.barber.name,
      'client': service.client.name,
      'created_at': service.created_at,
      'updated_at': service.updated_at
      } for service in get_services
    ]

    return format_services


  def update_service(self, id: int, Service_Update: Service_Update):

    get_service = self.db.query(Service).filter(Service.id == id).first()

    if not get_service:
      return 'Service not found'

    for key, value in Service_Update.__dict__.items():
      setattr(get_service, key, value)

    self.db.commit()
    self.db.refresh(get_service)

    return get_service


  def delete_service(self, id: int):

    get_service = self.db.query(Service).filter(Service.id == id).first()

    if not get_service:
      return 'Service not found'

    self.db.delete(get_service)
    self.db.commit()

    return 'Service deleted'