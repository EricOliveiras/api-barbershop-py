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


@router_service.get('/get-service-by-id/{id}')
def get_service_by_id(id: int, db: Session = Depends(get_db)):
  return ServiceController(db).get_service_by_id(id)


@router_service.get('/get-service-by-date/{date}')
def get_service_by_date(date: str, db: Session = Depends(get_db)):  
  return ServiceController(db).get_service_by_date(date)


@router_service.patch('/update-service/{id}')
def update_service(id: int, service: Service_Update, db: Session = Depends(get_db)):
  return ServiceController(db).update_service(id, service)


@router_service.delete('/delete-service/{id}')
def delete_service(id: int, db: Session = Depends(get_db)):
  return ServiceController(db).delete_service(id)