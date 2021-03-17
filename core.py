
import processing.processing as proc
import processing.typeconversion as tc


def core_addition(data: str) -> str:

    """
    Receives a json string, converts it to a dictionary and passes it to the processes.addition function.
    The returned sum gets converted to a dictionary which is returned 

    :param data: string in json format
    :type data: str

    :return: A string in json format with the key "sum" and the sum of two numbers as value
    """
    
    if(type(data) != dict):
        dict_data = tc.json_to_dict(data)
    else:
        dict_data = data
    
    sum = proc.addition(dict_data["number1"], dict_data["number2"])
    json_return = tc.dict_to_json(sum)

    return json_return


def get_components() ->str :

    #components = getFromDatabaseORM_Method 
    # compontents dict_to_json

    return components

def component_delete(data: str):
    data = json_to_dict(data)

    #dic_return = deleteCompontent(data)
    #return dict_to_json(dic_return)
    pass