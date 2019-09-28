from api import app,jsonify,request,session
from api.models import Customer
global session
class Customer_methods:
    @staticmethod
    def check_user_existance_and_apply(function_to_apply,c1_json):
        if session.query(Customer).filter(Customer.email==c1_json["email"]).first() != None:
            message=function_to_apply(c1_json)#patch, put, delete,get not post
            session.commit()
            return (jsonify(message),200)
        else:
            return (jsonify({"message":"Bad request buddy."}),400)
    @staticmethod
    def get_user(c1_json):
        a_user=session.query(Customer).filter(Customer.email==c1_json["email"]).first()
        return {"name":a_user.name,"address":a_user.address,"email":a_user.email}
    @staticmethod
    def replace_user(c1_json):
        session.delete(Customer).filter(Customer.email==c1_json["email"]).first()
        c1=Customer(name = c1_json["name"], address = c1_json["address"], email = c1_json["email"])
        session.add(c1)
        return {"message":"User succesfully replaced."}
    @staticmethod
    def patch_user(c1_json):
        session.query(Customer).filter(Customer.email==c1_json["email"]).first()
        return {"message":"User succesfully updated."}
    @staticmethod
    def delete_user(c1_json):
        session.delete(session.query(Customer).filter(Customer.email==c1_json["email"]).first())
        return {"message":"User succesfully deleted."}
@app.route('/', methods=['GET'])
def get():
    c1_json = request.get_json()
    return Customer_methods.check_user_existance_and_apply(Customer_methods.get_user,c1_json)
@app.route('/', methods=['POST'])
def post():
    c1_json = request.get_json()
    if session.query(Customer).filter(Customer.email==c1_json["email"]).first() == None:
        c1=Customer(name = c1_json["name"], address = c1_json["address"], email = c1_json["email"])
        session.add(c1)
        session.commit()
        return (jsonify({"message":"Successfully loaded."}),200)
    else:
        return (jsonify({"message":"This email already exists."}),404)

@app.route('/',methods=['PUT'])
def patch():
    c1_json = request.get_json()
    one_customer=session.query(Customer).filter(Customer.email==c1_json["email"]).first()
    if one_customer == None:
        return (jsonify({"message":"Mail not found."}),404)
    else:
        session.add(one_customer)
        session.commit()
        return (jsonify({}),200)
@app.route('/',methods=['DELETE'])
def delete():
    c1_json = request.get_json()
    return Customer_methods.check_user_existance_and_apply(Customer_methods.delete_user,c1_json)