# external endpoints
from flask import Flask, render_template,request
from core import core_addition, get_components, component_delete

app = Flask(__name__, static_url_path='', template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/addition', methods=["POST"])
def addition_route():
    """
       Test API endpoint for addition
       :recives data via POST request from frontend containing 2 numbers
       :returns a JSON object containing the sum of the parameters in request body
       """
    if request.is_json:
        try:
            return core_addition(request.json),200

        except:
            return "Internal Error",500
    else :
        return "No JSON body was transferred",400

@app.route("/component/overview", methods=["GET"])
def get_component_overview():
    """
    API Endpoint returning all components for the Index site
    :receives None
    :returns a JSON object containing a list of components
    """
    
    components = get_components()
    
    return components

@app.route("/component/delete", methods=["POST"])
def do_component_delete():
    """API Endpoint to delete specific components

    Returns:
        str: In JSON Format
    """
    if request.is_json:
        try:
            return component_delete(request.json),200

        except:
            return "Internal Error",500
    else :
        return "No JSON body was transferred",400