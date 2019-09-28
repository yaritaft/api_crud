from flask import Flask,jsonify,request

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sales.db', echo = True)
from api.models import Customer,Base
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()


app = Flask(__name__)

from api import routes