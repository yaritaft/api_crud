from flask_restful import Api
from app import app
from Task import Task

def main():
    restServer = Api(app)

    restServer.add_resource(Task,'/api/v1.0/task')
