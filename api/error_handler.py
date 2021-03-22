import processing.typeconversion as typeconversion


def error_handler(error_status: int, error_message: str) -> str:
    """
    Creates and returns an error JSON object

    :param error_status: The error status, e.g. 500
    :type error_status: int
    :param error_message: The error message briefly explaining the error occurrence
    :type error_message: str
    :return: JSON object (string) containing the error data
    """

    error_response = {
        "success": False,
        "error_status": error_status,
        "error_message": error_message
    }

    return typeconversion.dict_to_json(error_response)
