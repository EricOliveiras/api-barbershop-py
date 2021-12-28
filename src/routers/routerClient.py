from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.schemas.ClientBase import Client_Base, Client_Update
from src.controllers.ClientController import ClientController
from src.database.config.connect import get_db

router_client = APIRouter()


@router_client.post('/create-client')
def create_client(client: Client_Base, db: Session = Depends(get_db)):
  return ClientController(db).create_client(client)


@router_client.get('/get-all-clients')
def get_all_clients(db: Session = Depends(get_db)):
  return ClientController(db).get_all_clients()


@router_client.get('/get-client-by-id/{id}')
def get_client_by_id(id: int, db: Session = Depends(get_db)):
  return ClientController(db).get_client_by_id(id)


@router_client.get('/get-client-by-email/{email}')
def get_client_by_email(email: str, db: Session = Depends(get_db)):
  return ClientController(db).get_client_by_email(email)


@router_client.patch('/update-client/{id}')
def update_client(id: int, client: Client_Update, db: Session = Depends(get_db)):
  return ClientController(db).update_client(id, client)


@router_client.delete('/delete-client/{id}')
def delete_client(id: int, db: Session = Depends(get_db)):
  return ClientController(db).delete_client(id)