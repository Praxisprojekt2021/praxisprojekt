
import processing.processing as proc
import processing.typeconversion as tc

import database.handler.component_handler as component_handler


def core_addition(data: str) -> str:
    """
    Receives a json string, converts it to a dictionary and passes it to the processes.addition function.
    The returned sum gets converted to a dictionary which is returned 

    :param data: string in json format
    :type data: str

    :return: A string in json format with the key "sum" and the sum of two numbers as value
    """

    if(type(data) != dict):
        dict_data = tc.json_to_dict(data)
    else:
        dict_data = data

    sum = proc.addition(dict_data["number1"], dict_data["number2"])
    json_return = tc.dict_to_json(sum)

    return json_return


def get_components() -> str:
    """Calls the get_compontent_list method and converts the output to JSON

    Returns:
        str: A JSON formatted compontent list
    """
    components = component_handler.get_component_list()

    return tc.dict_to_json(components)


def component_delete(data: str) -> str:
    """Calls the delete_component method and returns whether successful or not in JSON Format

    Args:
        data (str): String in JSON Format

    Returns:
        (str): String in JSON Format
    """
    data = json_to_dict(data)

    dic_return = component_handler.delete_component(data)
    return tc.dict_to_json(dic_return)
