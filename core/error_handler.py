def error_handler(error_status: int, error_message: str) -> dict:
    """
    Creates and returns an error dict

    :param error_status: The error status, e.g. 500
    :type error_status: int
    :param error_message: The error message briefly explaining the error occurrence
    :type error_message: str
    :return: dict
    """

    error_response = {
        "success": False,
        "error_status": error_status,
        "error_message": error_message
    }

    return error_response
