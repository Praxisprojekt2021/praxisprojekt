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
    
    return typeconversion.dict_to_json(result)


def core_component_create_edit(input_object: str) -> str:
    """
    Receives a JSON object in the form defined under JSON_objects_defitnions.py for either editing a component or creating a new component
    The answer is also a JSON object, only containing the success state, which is True or False
    
    :param input_object: JSON object containing all component attributes (special information to differentiate edit or create is contained in the ID, which is either -1 or the original ID
    :type input_object: str
    :return A JSON object containing the success state, which is True or False
    """
    
    data_dict = typeconversion.json_to_dict(input_object)
    result = {}
    
    if data_dict["id"] == -1:
        result = component_handler.add_component(data_dict)
    elif data_dict["id"] >= 0:
        result = component_handler.edit_component(data_dict)
    else:
        result = {"success": False} # Optionally it could be cleaner to import the result object in the else case directly from a template
    
    return typeconversion.dict_to_json(result)
