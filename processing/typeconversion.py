
import json
from typing import Dict, Any

def dict_to_json(dict_data: Dict[str, Any]) -> str:

    """
    Converts a python dictionary to a JSON string

    :param dict_data: Python dictionary with keys in string format and "any" value
    :return: Returns a JSON string
    """

    try:
        json_string = json.dumps(dict_data)
    except:
        print("error handler")
        return

    return json_string


def json_to_dict(json_data: str) -> Dict[str, Any]:

    """
    Converts a JSON string to a python dictionary

    :param json_data: JSON string
    :return: Returns a python dictionary with keys in string format and "any" value
    """

    try:
        dictionary = json.loads(json_data)
    except:
        print("error handler")
        return

    return dictionary

