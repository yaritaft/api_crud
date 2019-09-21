from sqlalchemy import create_engine
engine = create_engine('sqlite:///sales.db', echo = True)

from models import Customers,Base

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()