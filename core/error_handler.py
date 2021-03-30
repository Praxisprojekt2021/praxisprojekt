import processing


def error_handler(error_type: str, error_message: str) -> str:
    """
    Creates and returns an error dict

    :param error_type: The error name, e.g. TypeError
    :type error_type: str
    :param error_message: The error message briefly explaining the error occurrence
    :type error_message: str
    :return: str
    """

    error_response = {
        "success": False,
        "error_type": error_type,
        "error_message": error_message
    }

    return processing.dict_to_json(error_response)
