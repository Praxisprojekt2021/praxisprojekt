
import processing.processing as proc
import processing.typeconversion as tc


def core_addition(json_data: str) -> str:

    """
    Receives a json string, converts it to a dictionary and passes it to the processes.addition function.
    The returned sum gets converted to a dictionary which is returned 

    :param json_data: string in json format
    :type json_data: str

    :return: A string in json format with the key "sum" and the sum of two numbers as value
    """

    dict_data = tc.json_to_dict(json_data)
    sum = proc.addition(dict_data["num1"], dict_data["num2"])
    json_return = tc.dict_to_json(sum)

    return json_return


