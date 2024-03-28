from modules.loans.store.loan_store import LoanStore
from modules.loans.serializer import serialize_loan, serialize_loans

class LoansService:
    def __init__(self, store=None):
        self.store = store if store else LoanStore()

    def get_all(self, pagination_options):
        return serialize_loans(self.store.get_loans(pagination_options))

    def get_by_id(self, id):
        return serialize_loan(self.store.get_loan_by_id(id))

    def create(self, loan):
        return self.store.create_loan(loan)

    def update(self, id, loan):
        return self.store.update_loan(id, loan)

    def delete(self, id):
        return self.store.delete_loan(id)
