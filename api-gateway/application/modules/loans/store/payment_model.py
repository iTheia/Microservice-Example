from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LoanPayment(Base):
    __tablename__ = 'loan_payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    loan_id = Column(Integer, ForeignKey('loans.id'))
    amount = Column(DECIMAL(15, 2))
