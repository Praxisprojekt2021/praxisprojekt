import json
from typing import Dict, Any, Union


def dict_to_json(dictionary: Dict[str, Any]) -> str:
    """
    Converts a python dictionary to a JSON object

    :param dictionary: Python dictionary with keys in string format and "any" value
    :type dictionary: Dict[str, Any]
    :return: Returns a JSON object
    """

    if not isinstance(dictionary, dict):
        raise TypeError(f'The passed parameter "{dictionary}" is not a dictionary')

    return json.dumps(dictionary)
