from lib.base_repository import BaseRepository
from modules.loans.store.loan_model import Loan

"""
    TODO: proteger campos especificos por entidad que no deberian ser poder editados
"""
class LoansRepository(BaseRepository):
    def __init__(self):
        super().__init__(Loan)