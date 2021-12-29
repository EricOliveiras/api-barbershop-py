from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.schemas.ServiceBase import Service_Base, Service_Update
from src.controllers.ServiceController import ServiceController
from src.database.config.connect import get_db


router_service = APIRouter()

@router_service.post('/create-service')
def create_service(service: Service_Base, db: Session = Depends(get_db)):
  return ServiceController(db).create_service(service)


@router_service.get('/get-all-services')
def get_all_services(db: Session = Depends(get_db)):  
  return ServiceController(db).get_all_services()