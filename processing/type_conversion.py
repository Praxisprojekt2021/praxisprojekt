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


def json_to_dict(json_object: str) -> Union[Dict[str, Any], str]:
    """
    Converts a JSON object to a python dictionary
    :param json_object: JSON object
    :type json_object: str
    :return: Returns a python dictionary with keys in string format and "any" value
    """

    if isinstance(json_object, dict):
        raise TypeError("A dict instead of a JSON object was given")
    else:
        dictionary = json.loads(json_object)
        if isinstance(dictionary, dict):
            return dictionary
        else:
            raise TypeError("Could not convert JSON object to dict")
