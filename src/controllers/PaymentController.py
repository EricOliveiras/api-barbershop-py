from sqlalchemy.orm import Session
from functools import reduce
import operator

from src.database.models.Payment import Payment
from src.database.schemas.PaymentBase import Payment_Base, Payment_Update
from src.database.models.Service import Service
from src.database.models.Barber import Barber

class PaymentController:
  def __init__(self, db: Session):
    self.db = db

  def create_payment(self, payment_base: Payment_Base):

    id_barber = payment_base.barber_id  

    get_barber = self.db.query(Barber).filter(Barber.id == id_barber).first()
    get_services = self.db.query(Service).filter(Service.barber_id == id_barber).all()

    if not get_barber:
      return 'Barber not found'

    if get_services.__len__ == 0:
      return 'No services found'

    all_prices = [service.price for service in get_services]
    total_payment = reduce(operator.add, all_prices)

    if total_payment == 0:
      return 'There is not enough value to generate payment'

    new_payment = Payment(
      barber_id = id_barber,
      total_payment = total_payment,
    )

    self.db.add(new_payment)
    self.db.commit()
    self.db.refresh(new_payment)

    format_payment = {
      'id': new_payment.id,
      'barber_id': id_barber,
      'total_payment': total_payment,
      'created_at': new_payment.created_at,
      'updated_at': new_payment.updated_at
    }

    return format_payment