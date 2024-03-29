# external endpoints
from flask import Flask, render_template, request
import sys

import core.core as core
from core.error_handler import error_handler

app = Flask(__name__, static_url_path='',
            template_folder='../frontend/templates', static_folder='../frontend/static')


@app.route('/', methods=["GET"])
def index_route():
    """
    API endpoint to display main page view

    :receives: None
    :return: the rendered html main page
    """
    return render_template("index.html")


@app.route('/about', methods=["GET"])
def info_route():
    """
    API endpoint to display info page view

    :receives: None
    :return: the rendered html info page
    """
    return render_template("info.html")


"""
    API endpoints for component operations
"""


@app.route('/component', methods=["GET"])
def component_route():
    """
    API endpoint to display component page view

    :receives: None
    :return: the rendered html component page
    """
    return render_template("component.html")


@app.route("/component/overview", methods=["GET"])
def component_overview_route():
    """
    API Endpoint returning all components for the Index site

    :receives: None
    :return: a JSON object containing a list of components
    """

    components = core.get_component_list()

    return components


@app.route('/component/view', methods=["POST"])
def component_view_route():
    """
    API endpoint to use the function from the Core-Module to view components

    :receives: a JSON object with component details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object containing the component
    """

    if request.is_json:
        return core.get_component(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route('/component/create_edit', methods=["POST"])
def component_create_edit_route():
    """
    Use function from the Core-Module to create or edit components (Original function is located in component_handler.py

    :receives: a JSON object with component details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object containing the success state, which is True or False
    """

    if request.is_json:
        return core.create_edit_component(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route("/component/delete", methods=["POST"])
def component_delete_route():
    """
    API Endpoint to delete a specific component

    :receives: a JSON object with component details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object with the success of the deletion
    """

    if request.is_json:
        return core.delete_component(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


"""
    API endpoints for process operations 
"""


@app.route('/process', methods=["GET"])
def process_route():
    """
    API endpoint to display process page view

    :receives: None
    :return: the rendered html process page
    """
    return render_template("process.html")


@app.route('/process/overview', methods=["GET"])
def process_overview_route():
    """
    API Endpoint returning all processes for the Index site

    :receives: None
    :return: a JSON object containing a list of processes
    """

    processes = core.get_process_list()

    return processes


@app.route('/process/delete', methods=["POST"])
def process_delete_route():
    """
    API Endpoint to delete a specific process

    :receives: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object with the success of the deletion
    """

    if request.is_json:
        return core.delete_process(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route('/process/edit/createstep', methods=["POST"])
def process_edit_createstep_route():
    """
    API Endpoint to add a step to specific process

    :receives: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    """
    if request.is_json:
        return core.add_process_reference(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route('/process/edit/editstep', methods=["POST"])
def process_edit_editstep_route():
    """
    API Endpoint to edit a step from specific process

    :receives: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    """
    if request.is_json:
        return core.update_process_reference(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route('/process/edit/deletestep', methods=["POST"])
def process_edit_deletestep_route():
    """
    API Endpoint to delete a step from specific process

    :receives: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    """
    if request.is_json:
        return core.delete_process_reference(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route('/process/create_edit', methods=["POST"])
def process_create_edit_route():
    """
    API Endpoint to create or edit a process

    :receives: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    """
    if request.is_json:
        return core.create_edit_process(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


@app.route('/process/view', methods=["POST"])
def process_view_route():
    """
    API endpoint to use the function from the Core-Module to view processes

    :receives: a JSON object with process details as specified in docu/JSON_objects_definitions.py
    :return: a JSON object containing the process
    """
    if request.is_json:
        return core.get_process(request.json), 200
    else:
        raise TypeError("No JSON body was transferred")


"""
    Test Report Endpoints
"""


@app.route('/test/frontend', methods=["GET"])
def frontend_test_route():
    """
    API endpoint to display Frontend Report Page

    :receives: None
    :return: the rendered frontend report page page
    """
    return render_template("TestResults_FrontendTests.html")


@app.route('/test/unit', methods=["GET"])
def unit_test_route():
    """
    API endpoint to display Unittest Report Page

    :receives: None
    :return: the rendered unittest report page page
    """
    return render_template("TestsResults_UnitTests.html")


"""
    API Error Handlers
"""


@app.errorhandler(Exception)
def error_occurred(error):
    """
    API error handler
    :receives: None
    :return: an error JSON
    """
    exc_type, value, traceback = sys.exc_info()
    error_json = error_handler(exc_type.__name__, str(value))

    return error_json, 500


@app.errorhandler(404)
def page_not_found(error):
    """
    API error handler for pages that were not found

    :receives: None
    :return: an error message
    """

    return "Page was not found.", 404
