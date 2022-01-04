from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.schemas.PaymentBase import Payment_Base, Payment_Update
from src.controllers.PaymentController import PaymentController
from src.database.config.connect import get_db

router_payment = APIRouter()


@router_payment.post('/create-payment')
def create_payment(payment: Payment_Base, db: Session = Depends(get_db)):
  return PaymentController(db).create_payment(payment)