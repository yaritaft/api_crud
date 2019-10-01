from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class Customer(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)
   @staticmethod
   def check_user_existance_and_apply(c1_json,session):
      return session.query(Customer).filter(Customer.email==c1_json["email"]).first() != None