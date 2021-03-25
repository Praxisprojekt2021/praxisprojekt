from typing import Dict, Any, Union

import database.handler.process_handler as process_handler
import database.handler.component_handler as component_handler

import processing


def get_component_list() -> str:
    """
    Calls the get_compontent_list method and converts the output to JSON

    :return: A JSON formatted compontent list
    """
    component_list_dict = component_handler.get_component_list()
    output_json = processing.dict_to_json(component_list_dict)

    return output_json


def get_component(input_object: str) -> str:
    """
    Receives a JSON object in the form defined under JSON_objects_defitnions.py for getting/viewing a component.
    It returns another JSON object, sturctured as described in docu/JSON_objects_definitions.py
    which is retreived from the component_handler.

    :param input_object: JSON object containing the component uid
    :type input_object: str
    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py
    """

    data_dict = processing.json_to_dict(input_object)
    component_dict = component_handler.get_component(data_dict)
    output_json = processing.dict_to_json(component_dict)

    return output_json


def create_edit_component(input_object: Union[Dict[str, Any], str]) -> str:
    """
    Receives a JSON object in the form defined under JSON_objects_defitnions.py for either editing a component or creating a new component
    The answer is also a JSON object, only containing the success state, which is True or False
    
    :param input_object: JSON object containing all component attributes (special information to differentiate edit or create is contained in the UID, which is either -1 or the original UID
    :type input_object: str
    :return: A JSON object containing the success state, which is True or False
    """

    data_dict = processing.json_to_dict(input_object)

    if data_dict["uid"] == "-1":
        result_dict = component_handler.add_component(data_dict)
        return processing.dict_to_json(result_dict)
    else:
        result_dict = component_handler.update_component(data_dict)
        return processing.dict_to_json(result_dict)


def delete_component(input_object: str) -> str:
    """
    Calls the delete_component method and returns whether successful or not in JSON Format

    :param input_object: JSON object containing the component uid
    :type input_object: str
    :return: String in JSON Format
    """

    data_dict = processing.json_to_dict(input_object)
    result_dict = component_handler.delete_component(data_dict)
    output_json = processing.dict_to_json(result_dict)

    return output_json


def get_process_list() -> str:
    """
    Calls the get_process_list method and converts the output to JSON

    :return: A JSON formatted compontent list
    """
    process_list_dict = process_handler.get_process_list()
    output_json = processing.dict_to_json(process_list_dict)

    return output_json


def get_process(input_object: str) -> str:
    """
    Receives a JSON object in the form defined under JSON_objects_defitnions.py for getting/viewing a process.
    It returns another JSON object, sturctured as described in docu/JSON_objects_definitions.py
    which is retreived from the process_handler.

    :param input_object: JSON object containing the process uid
    :type input_object: str
    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py
    """
    data_dict = processing.json_to_dict(input_object)
    process_dict = process_handler.get_process(data_dict)
    output_json = processing.dict_to_json(process_dict)

    #TO DO Risk Calculation on output_json

    data = {
        "success": True,
        "process": {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde anlegen",
            "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            "components": [
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
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
        "should-metrics": {
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


def create_edit_process(input_object: Union[Dict[str, Any], str]) -> str:
    """
    Receives a JSON object in the form defined under JSON_objects_defitnions.py for either editing a process or creating a new process
    The answer is also a JSON object containing either the success state if False, otherwise calls get_process
    
    :param input_object: JSON object containing all process attributes (special information to differentiate edit or create is contained in the UID, which is either -1 or the original UID
    :type input_object: str
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    data_dict = processing.json_to_dict(input_object)

    if data_dict["uid"] == "-1":
        result_dict = process_handler.add_process(data_dict)
        if result_dict["success"]== True:
            return get_process(result_dict["process_uid"])
        else:
            return processing.dict_to_json(result_dict)
    else:
        result_dict = process_handler.update_process(data_dict)
        if result_dict["success"]== True:
            return get_process(data_dict["uid"])
        else:
            return processing.dict_to_json(result_dict)


def delete_process(input_object: str) -> str: 
    """
    Calls the delete_process method and returns whether successful or not in JSON Format

    :param input_object: JSON object containing the process uid
    :type input_object: str
    :return: String in JSON Format
    """

    data_dict = processing.json_to_dict(input_object)
    result_dict = process_handler.delete_process(data_dict)
    output_json = processing.dict_to_json(result_dict)

    return output_json


def add_process_reference(input_object: str]) -> str:
    """
    Calls the add_process_reference method and returns whether successful or not in JSON Format

    :param input_object: JSON object containing the process uid + component uid + weight 
    :type input_object: str
    :return: String in JSON Format
    """

    data_dict = processing.json_to_dict(input_object)

    result_dict = process_handler.add_process_reference(data_dict)

    if result_dict["success"]== True:
        return get_process(data_dict["uid"])
    else:
        return processing.dict_to_json(result_dict)


def update_process_reference(input_object: str]) -> str:
    """
    Calls the update_process_reference method and returns whether successful or not in JSON Format

    :param input_object: JSON object containing the process uid + old_weight + new_weight
    :type input_object: str
    :return: String in JSON Format
    """

    data_dict = processing.json_to_dict(input_object)

    result_dict = process_handler.update_process_reference(data_dict)

    if result_dict["success"]== True:
        return get_process(data_dict["uid"])
    else:
        return processing.dict_to_json(result_dict)


def delete_process_reference(input_object: str]) -> str:
    """
    Calls the delete_process_reference method and returns whether successful or not in JSON Format

    :param input_object: JSON object containing the process uid + weight
    :type input_object: str
    :return: String in JSON Format
    """

    data_dict = processing.json_to_dict(input_object)

    result_dict = process_handler.delete_process_reference(data_dict)

    if result_dict["success"]== True:
        return get_process(data_dict["uid"])
    else:
        return processing.dict_to_json(result_dict)
