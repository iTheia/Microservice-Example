from modules.loans.store.loan_repository import LoansRepository
from modules.loans.store.payment_repository import LoanPaymentRepository


class LoanStore:
  def __init__(self, LoanRepository=None, PaymentRepository=None):
      self.LoanRepository = LoanRepository if LoanRepository else LoansRepository()
      self.PaymentRepository = PaymentRepository if PaymentRepository else LoanPaymentRepository()

  def create_loan(self, data):
     return self.LoanRepository.create(data)

  def update_loan(self, id, data):
     return self.LoanRepository.update(id, data)

  def delete_loan(self, id):
     return self.LoanRepository.delete(id)

  def get_loan_by_id(self, id):
     return self.LoanRepository.get_by_id(id)

  def get_loans(self, pagination_options):
     return self.LoanRepository.get_all(pagination_options)
