def serialize_loan(loan):
  return {
    'id': loan.id,
    'client': loan.client_id,
    'amount': loan.amount,
    'start_date': loan.start_date,
    'end_date': loan.end_date,
    'interest_rate': loan.interest_rate,
    'status': loan.status,
  }

def serialize_loans(loans):
  return [serialize_loan(loan) for loan in loans]