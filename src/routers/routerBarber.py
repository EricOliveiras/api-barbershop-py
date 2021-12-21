from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.schemas.BarberBase import BarberBase
from src.controllers.BarberController import BarberController
from src.database.config.connect import get_db

router = APIRouter()

@router.post('/create-barber')
def create_barber(barber: BarberBase, db: Session = Depends(get_db)):
  return BarberController(db).create_barber(barber)

@router.get('/get-all-barbers')
def get_all_barbers(db: Session = Depends(get_db)):
  return BarberController(db).get_all_barbers()
