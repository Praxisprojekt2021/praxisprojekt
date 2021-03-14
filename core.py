
import processing.processing as proc
import processing.typeconversion as tc


def core_addition(data: str) -> str:

    """
    Receives a JSON object, converts it to a dictionary and passes it to the processes.addition function.
    The returned sum gets converted to a dictionary which is returned as JSON object

    :param data: JSON object containing two numbers
    :type data: str

    :return: A JSON object with the key "sum" and the sum of two numbers as value
    """
    
    if type(data) != dict:
        dict_data = tc.json_to_dict(data)
    else:
        dict_data = data
    
    sum = proc.addition(dict_data["number1"], dict_data["number2"])
    json_return = tc.dict_to_json(sum)

    return json_return
