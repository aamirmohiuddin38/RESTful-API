from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def project_info():
    return "RESTful API basic project"

if __name__ == "__main__":
    app.run(debug=True)