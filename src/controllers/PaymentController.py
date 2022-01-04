from sqlalchemy.orm import Session

from src.database.models.Payment import Payment
from src.database.schemas.PaymentBase import Payment_Base, Payment_Update
from src.database.models.Service import Service
from src.database.models.Barber import Barber

class PaymentController:
  def __init__(self, db: Session):
    self.db = db

  def create_payment(self, id_barber: int):

    get_barber = self.db.query(Barber).filter(Barber.id == id_barber).first()
    
    if not get_barber:
      return 'Barber not found'

    get_service = self.db.query(Service).filter(Service.barber_id == id_barber).all()

    if not get_service:
      return 'Service not found'

    total_payment = get_service.__reduce__((lambda x, y: x + y, 0))

    payment = Payment(
      barber_id = id_barber,
      total_payment = total_payment
    )

    self.db.add(payment)
    self.db.commit()
    self.db.refresh(payment)