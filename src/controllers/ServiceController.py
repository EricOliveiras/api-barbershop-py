from sqlalchemy.orm import Session

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
    else:
      return get_services