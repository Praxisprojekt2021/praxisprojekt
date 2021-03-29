import database.handler.process_handler as process_handler
import database.handler.component_handler as component_handler

import processing


def get_component_list() -> str:
    """
    Calls the get_component_list method and converts the output to JSON

    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py
    """
    component_list_dict = component_handler.get_component_list()
    output_json = processing.dict_to_json(component_list_dict)

    return output_json


def get_component(input_dict: dict) -> str:
    """
    Receives a dict in the form defined under JSON_objects_definitions.py for getting/viewing a component.
    It returns another JSON object, structured as described in docu/JSON_objects_definitions.py
    which is retrieved from the component_handler.

    :param input_dict: dict containing the component uid
    :type input_dict: dict
    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py representing a component
    """

    component_dict = component_handler.get_component(input_dict)
    output_json = processing.dict_to_json(component_dict)

    return output_json


def create_edit_component(input_dict: dict) -> str:
    """
    Receives a dict in the form defined under JSON_objects_definitions.py for either
    editing a component or creating a new component
    The answer is a JSON object, only containing the success state, which is True or False
    
    :param input_dict: dict containing all component attributes (special information
    to differentiate edit or create is contained in the UID, which is either -1 or the original UID
    :type input_dict: dict
    :return: A JSON object containing the success state, which is True or False
    """

    if input_dict["uid"] == "-1":
        result_dict = component_handler.add_component(input_dict)
        return processing.dict_to_json(result_dict)
    else:
        result_dict = component_handler.update_component(input_dict)
        return processing.dict_to_json(result_dict)


def delete_component(input_dict: dict) -> str:
    """
    Calls the delete_component method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the component uid
    :type input_dict: dict
    :return: A JSON object containing the success state, which is True or False
    """

    result_dict = component_handler.delete_component(input_dict)
    output_json = processing.dict_to_json(result_dict)

    return output_json


def get_process_list() -> str:
    """
    Calls the get_process_list method and converts the output to JSON

    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py
    representing a process list
    """
    process_list_dict = process_handler.get_process_list()
    output_json = processing.dict_to_json(process_list_dict)

    return output_json


def get_process(input_dict: dict) -> str:
    """
    Receives a dict in the form defined under JSON_objects_definitions.py for getting/viewing a process.
    It returns a JSON object, structured as described in docu/JSON_objects_definitions.py
    which is retrieved from the process_handler.

    :param input_dict: dict containing the process uid
    :type input_dict: dict
    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py representing a process
    """

    process_dict = process_handler.get_process(input_dict)
    output_json = processing.dict_to_json(process_dict)

    # TO DO Risk Calculation on output_json

    data = {
        "success": True,
        "process": {
            "uid": "b141f94973a43cf8ee972e9dffc1b014",
            "name": "Kunde anlegen",
            "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            "components": [
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b014",
                    "weight": 1,  # different from single component view!
                    "name": "SQL Datenbank",
                    "category": "Datenbank",
                    "description": "Kundendatenbank",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "codelines": 20000,
                        "admins": 10,
                        "recovery_time": 5
                    }
                },
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
                    "weight": 1.5,
                    "name": "Frontend API",
                    "category": "API",
                    "description": "API für das Frontend",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "codelines": 20000,
                        "admins": 10,
                        "recovery_time": 5
                    }
                },
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
                    "weight": 2,
                    "name": "Hadoop Cluster",
                    "category": "Datenbank",
                    "description": "Big Data Plattform",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "codelines": 20000,
                        "admins": 10,
                        "recovery_time": 5
                    }
                }
            ]
        },
        "target_metrics": {
            "codelines": 25000,
            "admins": 12,
            "recovery_time": 3
        },
        "score": 80,  # percent as integer
        "actual_metrics": {
            "codelines": {
                "value": 30,
                "fulfillment": True
            },  # true means that the metric is fulfilled --> no problem.
            "admins": {
                "value": 30,
                "fulfillment": True
            },
            "recovery_time": {
                "value": 20,
                "fulfillment": False
            },  # false means that the metric is not fulfilled --> problem.
        },
    }
    
    return processing.dict_to_json(data)


def create_edit_process(input_dict: dict) -> str:
    """
    Receives a dict in the form defined under JSON_objects_definitions.py for either
    editing a process or creating a new process
    The answer is a JSON object containing either the success state if False, otherwise calls get_process
    
    :param input_dict: dict containing all process attributes (special information
    to differentiate edit or create is contained in the UID, which is either -1 or the original UID
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    if input_dict["uid"] == "-1":
        result_dict = process_handler.add_process(input_dict)
        output_object = get_process(result_dict["process_uid"])
        return output_object
    else:
        result_dict = process_handler.update_process(input_dict)
        output_object = get_process(input_dict["uid"])
        return output_object


def delete_process(input_dict: dict) -> str:
    """
    Calls the delete_process method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the process uid
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    result_dict = process_handler.delete_process(input_dict)
    output_json = processing.dict_to_json(result_dict)

    return output_json


def add_process_reference(input_dict: dict) -> str:
    """
    Calls the add_process_reference method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the process uid + component uid + weight
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    result_dict = process_handler.add_process_reference(input_dict)
    output_object = get_process(input_dict["uid"])
    return output_object


def update_process_reference(input_dict: dict) -> str:
    """
    Calls the update_process_reference method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the process uid + old_weight + new_weight
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    result_dict = process_handler.update_process_reference(input_dict)
    output_object = get_process(input_dict["uid"])
    return output_object


def delete_process_reference(input_dict: dict) -> str:
    """
    Calls the delete_process_reference method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the process uid + weight
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    result_dict = process_handler.delete_process_reference(input_dict)
    output_object = get_process(input_dict["uid"])
    return output_object
