
from sqlalchemy import Column, Integer, String, Text, Date
from database import Base
class Customer(Base):
  __tablename__ = "customers"
  id = Column(Integer,primary_key=True, index=True)
  name = Column(String, nullable=False)
  contact = Column(String, nullable=False)
  company = Column(String, nullable=True)
  last_interaction = Column(Date, nullable=True)
  next_followup = Column(Date, nullable=True)
  status = Column(String, nullable=True)
  interest_level = Column(String,nullable=True)
  notes = Column(Text, nullable=True)
  