from lib.base_repository import BaseRepository
from modules.loans.store.payment_model import LoanPayment

"""
    TODO: proteger campos especificos por entidad que no deberian ser poder editados
"""
class LoanPaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__(LoanPayment)