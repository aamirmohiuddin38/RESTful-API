from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if functionName == "add":
        if "x" not in postedData or "y" not in postedData:
            return 301
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

api.add_resource(Add, "/add")

@app.route('/')
def project_info():
    return "RESTful API basic project"

if __name__ == "__main__":
    app.run(debug=True)