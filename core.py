import processing.calculations as calculations
import processing.typeconversion as typeconversion


def core_addition(input_object: str) -> str:
    """
    Receives a JSON object, converts it to a dictionary and passes it to the calculations.addition function.
    The returned sum gets converted to a dictionary which is returned as JSON object

    :param input_object: JSON object containing two numbers
    :type input_object: str
    :return: A JSON object with the key "sum" and the sum of two numbers as value
    """
    
    data_dict = typeconversion.json_to_dict(input_object)
    result = calculations.addition(data_dict["number1"], data_dict["number2"])
    output_object = typeconversion.dict_to_json(result)

    return output_object
