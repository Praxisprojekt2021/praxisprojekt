import json
from typing import Dict, Any, Union

from core.error_handler import error_handler


def dict_to_json(dictionary: Dict[str, Any]) -> str:
    """
    Converts a python dictionary to a JSON object

    :param dictionary: Python dictionary with keys in string format and "any" value
    :type dictionary: Dict[str, Any]
    :return: Returns a JSON object
    """

    return json.dumps(dictionary)
