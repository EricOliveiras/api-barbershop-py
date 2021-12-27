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

