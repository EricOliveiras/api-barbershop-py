from sqlalchemy.orm import Session

from src.database.models.Client import Client
from src.database.schemas.ClientBase import Client_Base, Client_Update


class ClientController:
  def __init__(self, db: Session):
    self.db = db

  def create_client(self, Client_Base: Client_Base):
    
    client_exist = self.db.query(Client).filter(Client.email == Client_Base.email).first()

    if not client_exist:
      new_client = Client(
        name = Client_Base.name,
        email = Client_Base.email,
        phone = Client_Base.phone
      )

      self.db.add(new_client)
      self.db.commit()
      self.db.refresh(new_client)

      return new_client

    else:
      return 'Client already exists'

  
  def get_all_clients(self):

    get_clients = self.db.query(Client).all()

    if get_clients.__len__ == 0:
      return 'No clients found'
    else:
      return get_clients


  def get_client_by_id(self, id: int):

    get_client = self.db.query(Client).filter(Client.id == id).first()

    if not get_client:
      return 'Client not found'
    else:
      return get_client


  def get_client_by_email(self, email: str):

    get_client = self.db.query(Client).filter(Client.email == email).first()

    if not get_client:
      return 'Client not found'
    else:
      return get_client


  def update_client(self, id: int, client_update: Client_Update):

    get_client = self.db.query(Client).filter(Client.id == id).first()

    if not get_client:
      return 'Client not found'

    for key, value in client_update.__dict__.items():
      setattr(get_client, key, value) if value else None

    self.db.commit()
    self.db.refresh(get_client)

    return get_client


  def delete_client(self, id: int):

    get_client = self.db.query(Client).filter(Client.id == id).first()

    if not get_client:
      return 'Client not found'

    self.db.delete(get_client)
    self.db.commit()

    return 'Client deleted'