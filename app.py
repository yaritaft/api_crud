from flask import Flask
import logging as logger
from flask_restful import Resource,reqparse,Api
import logging as logger
parser = reqparse.RequestParser()

class Task(Resource):
    def get(self):
        logger.debug('Inside get method')
        return {"hola":'chau'},200
    def post(self):
        parser.add_argument('nombre')
        args=parser.parse_args()
        return args

logger.basicConfig(level="DEBUG")


app = Flask(__name__)

restServer = Api(app)

restServer.add_resource(Task,'/api/v1.0/task')

if __name__=="__main__":
    logger.debug('Starting app.')
    app.run(host='127.0.0.1',port=8080,debug=True,use_reloader=True)

