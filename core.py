import processing.calculations as calculations
import processing.typeconversion as typeconversion
import database.handler.component_handler as component_handler


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


def get_components() -> str:
    """Calls the get_compontent_list method and converts the output to JSON

    Returns:
        str: A JSON formatted compontent list
    """
    component_list = component_handler.get_component_list()
    output_object = typeconversion.dict_to_json(component_list)

    return output_object


def component_delete(input_object: str) -> str:
    """Calls the delete_component method and returns whether successful or not in JSON Format

    Args:
        data (str): String in JSON Format

    Returns:
        (str): String in JSON Format
    """
    data_dict = typeconversion.json_to_dict(input_object)

    success = component_handler.delete_component(data_dict)
    output_object = typeconversion.dict_to_json(success)

    return output_object
