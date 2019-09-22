from api import app,jsonify,request,session
from api.models import Customers

@app.route('/', methods=['GET'])
def get():
    names=[]
    for one_customer in session.query(Customers).all():
        names.append(one_customer.name)
    return (jsonify({"Customers":names}),200)
@app.route('/', methods=['POST'])
def post():
    c1_json = request.get_json()
    try:
        c1=Customers(name = c1_json["name"], address = c1_json["address"], email = c1_json["email"])
        session.add(c1)
        session.commit()
        return (jsonify({"message":"Successfully loaded."}),200)
    except:
        return (jsonify({"message":"Bad request buddy."}),400)
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