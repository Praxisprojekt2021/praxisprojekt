from flask import Flask, render_template, request

import core
from api.error_handler import error_handler


app = Flask(__name__, static_url_path='', template_folder='../frontend/templates', static_folder='../frontend/static')


@app.route('/', methods=["GET"])
def index():
    """
    API endpoint to display main page view

    :return: the rendered html main page
    """
    return render_template("index.html")


@app.route('/addition', methods=["POST"])
def addition_route():
    """
    Test API endpoint for addition, that receives data via POST request from frontend containing 2 numbers

    :return: a JSON object containing the sum of the parameters in request body
    """

    if request.is_json:
        return core.core_addition(request.json), 200
    else:
        return error_handler(400, "No JSON body was transferred")


@app.route('/component/create_edit', methods=["POST"])
def component_create_edit_route():
    """
    Use function from the Core-Module to create or edit components (Original function is located in component_handler.py
    """
    
    if request.is_json:
        return core.core_component_create_edit(request.json), 200
    else:
        return error_handler(400, "No JSON body was transferred")
