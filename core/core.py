import database.handler.process_handler as process_handler
import database.handler.component_handler as component_handler
import database.handler.metric_handler as metric_handler

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


def get_process_list(score: int, components_count: int) -> str:
    """
    Calls the get_process_list method and converts the output to JSON after adding a score and a components count

    :param score: Score, to be added to the process list
    :type score: int
    :param components_count: Number of components, to be added to the process list
    :type components_count: int
    :return: Returns a JSON object, structured as described in docu/JSON_objects_definitions.py
    representing a process list
    """
    process_list_dict = process_handler.get_process_list()

    process_list_dict["process"]["score"] = score
    process_list_dict["process"]["components_count"] = components_count

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
    metrics_dict = metric_handler.get_metrics_data()

    output_dict = processing.calculations.start_calculate_risk(process_dict, metrics_dict)

    output_json = processing.dict_to_json(output_dict)
    
    return output_json


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
        output_object = get_process(process_handler.add_process(input_dict)["process_uid"])
        return output_object
    else:
        process_handler.update_process(input_dict)
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

    process_handler.add_process_reference(input_dict)

    output_object = get_process(input_dict["process_uid"])
    return output_object


def update_process_reference(input_dict: dict) -> str:
    """
    Calls the update_process_reference method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the process uid + old_weight + new_weight
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    process_handler.update_process_reference(input_dict)

    output_object = get_process(input_dict["uid"])
    return output_object


def delete_process_reference(input_dict: dict) -> str:
    """
    Calls the delete_process_reference method and returns whether successful or not in JSON Format

    :param input_dict: dict containing the process uid + weight
    :type input_dict: dict
    :return: A JSON object containing either the success state if False, otherwise calls get_process
    """

    process_handler.delete_process_reference(input_dict)

    output_object = get_process(input_dict["uid"])
    return output_object
