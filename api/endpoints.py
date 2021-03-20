from flask import Flask, render_template, request

import core
from api.error_handler import error_handler


app = Flask(__name__, static_url_path='',
            template_folder='../frontend/templates', static_folder='../frontend/static')


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


@app.route('/component/view', methods=["POST"])
def component_view_route():
    """
    API endpoint to use the function from the Core-Module to view components
    """

    if request.is_json:
        try:
            return core.component_view(request.json), 200
        except:
            return "Internal Error", 500
    else:
        return error_handler(400, "No JSON body was transferred")
