from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    amount = Column(DECIMAL(15, 2))
    start_date = Column(Date)
    end_date = Column(Date)
    interest_rate = Column(DECIMAL(5, 2))
    status = Column(String(20))

