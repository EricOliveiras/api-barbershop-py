from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.schemas.BarberBase import Barber_update, Barber_Base
from src.controllers.BarberController import BarberController
from src.database.config.connect import get_db

router = APIRouter()

@router.post('/create-barber')
def create_barber(barber: Barber_Base, db: Session = Depends(get_db)):
  return BarberController(db).create_barber(barber)


@router.get('/get-all-barbers')
def get_all_barbers(db: Session = Depends(get_db)):
  return BarberController(db).get_all_barbers()


@router.get('/get-barber-by-id/{id}')
def get_barber_by_id(id: int, db: Session = Depends(get_db)):
  return BarberController(db).get_barber_by_id(id)


@router.get('/get-barber-by-document/{document}')
def get_barber_by_document(document: str, db: Session = Depends(get_db)):
  return BarberController(db).get_barber_by_document(document)


@router.patch('/update-barber/{id}')
def update_barber(id: int, barber: Barber_update, db: Session = Depends(get_db)):
  return BarberController(db).update_barber(id, barber)


@router.delete('/delete-barber/{id}')
def delete_barber(id: int, db: Session = Depends(get_db)):
  return BarberController(db).delete_barber(id)