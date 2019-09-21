from flask import Flask,jsonify,request
from db import Customers,session
app = Flask(__name__)



@app.route('/', methods=['GET'])
def get():
    return jsonify({"elementos":elementos})
@app.route('/', methods=['POST'])
def post():
    c1_json = request.get_json()
    c1=Customers(name = c1_json["name"], address = c1_json["address"], email = c1_json["email"])
    session.add(c1)
    session.commit()
    return (jsonify({}),200)
@app.route('/',methods=['PUT'])
def put():
    for n,i in enumerate(elementos):
        if i["id"]==request.get_json()["id"]:
            elementos[n]["content"]=request.get_json()["content"]
    print(elementos)
    return (jsonify({}),200)
@app.route('/',methods=['DELETE'])
def delete():
    for n,i in enumerate(elementos):
        if i["id"]==request.get_json()["id"]:
            elementos.remove(elementos[n])
    print(elementos)
    return (jsonify({}),200)

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8080,debug=True,use_reloader=True)

