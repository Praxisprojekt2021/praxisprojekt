# external endpoints
from flask import Flask,request
from core import Core

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "Hier entsteht das Praxisprojekt 2021! Hallo!"

@app.route('/addition', methods=["POST"])
def addition_route():
    """
       Test API endpoint for addition

       :recives data via POST request from frontend containing 2 numbers

       :returns a JSON object containing the sum of the parameters in request body
       """
    if request.is_json:
        try:
            core_object = Core()
            return core_object.addition(request.json),200

        except:
            return "Internal Error",500
    else :
        return "No JSON body was transferred",400
