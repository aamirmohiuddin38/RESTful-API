from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if functionName == "add" or functionName == "sub" or functionName == "mult":
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif functionName == "div":
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        #Get the postedData
        postedData = request.get_json()

        #Check if data is sent or not
        statusCode = checkPostedData(postedData, "add")
        if (statusCode != 200):
            retJson = {
                "Message" : "Error happened  missing argument",
                "Status Code" : statusCode
            }
            return jsonify(retJson)

        num1 = postedData["x"]
        num2 = postedData["y"]
        
        #Convert data to int types if not
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2

        retMap = {
            "Message" : result,
            "Status Code" : statusCode
        }
        return jsonify(retMap)
    
class Subtract(Resource):
    def post(self):
        #Get the postedData
        postedData = request.get_json()

        #Check if data is sent or not
        statusCode = checkPostedData(postedData, "sub")
        if (statusCode != 200):
            retJson = {
                "Message" : "Error happened  missing argument",
                "Status Code" : statusCode
            }
            return jsonify(retJson)

        num1 = postedData["x"]
        num2 = postedData["y"]
        
        #Convert data to int types if not
        num1 = int(num1)
        num2 = int(num2)
        result = num1 - num2

        retMap = {
            "Message" : result,
            "Status Code" : statusCode
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #Get the postedData
        postedData = request.get_json()

        #Check if data is sent or not
        statusCode = checkPostedData(postedData, "mult")
        if (statusCode != 200):
            retJson = {
                "Message" : "Error happened  missing argument",
                "Status Code" : statusCode
            }
            return jsonify(retJson)

        num1 = postedData["x"]
        num2 = postedData["y"]
        
        #Convert data to int types if not
        num1 = int(num1)
        num2 = int(num2)
        result = num1 * num2

        retMap = {
            "Message" : result,
            "Status Code" : statusCode
        }
        return jsonify(retMap)
    
class Divide(Resource):
    def post(self):
        #Get the postedData
        postedData = request.get_json()

        #Check if data is sent or not
        statusCode = checkPostedData(postedData, "div")
        if(statusCode == 302):
            retJson = {
                "Message" : "Division By Zero Error",
                "Status Code" : statusCode
            }
            return jsonify(retJson)
        elif (statusCode != 200):
            retJson = {
                "Message" : "Error happened  missing argument",
                "Status Code" : statusCode
            }
            return jsonify(retJson)

        num1 = postedData["x"]
        num2 = postedData["y"]
        
        #Convert data to int types if not
        num1 = int(num1)
        num2 = int(num2)
        result = (num1*1.0) / num2          #multiply by float to make it float

        retMap = {
            "Message" : result,
            "Status Code" : statusCode
        }
        return jsonify(retMap)
    

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route('/')
def project_info():
    return "RESTful API basic project"

if __name__ == "__main__":
    app.run(host="0.0.0.0")