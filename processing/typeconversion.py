
import json
from typing import Dict, Any, Union

def dict_to_json(dict_data: Dict[str, Any]) -> Union[str, bool]:

    """
    Converts a python dictionary to a JSON string

    :param dict_data: Python dictionary with keys in string format and "any" value
    :return: Returns a JSON string
    """

    try:
        json_string = json.dumps(dict_data)
    except:
        error_val = error_handler()
        return error_val

    return json_string


def json_to_dict(json_data: str) -> Union[Dict[str, Any], bool]:

    """
    Converts a JSON string to a python dictionary

    :param json_data: JSON string
    :return: Returns a python dictionary with keys in string format and "any" value
    """

    try:
        dictionary = json.loads(json_data)
    except:
        error_val = error_handler()
        return error_val

    return dictionary


def error_handler() -> bool:
    return False