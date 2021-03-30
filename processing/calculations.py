from typing import Dict, Any


def start_calculate_risk(process_dict: Dict[str, Any], metrics_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    The entry function and handler for the risk calculations. The risk score is calculated and returned with all related
    values.

    :param metrics_dict: A dict containing all relevant data for the metrics
    :type metrics_dict: Dict[str: Any]
    :param process_dict: A dict containing all relevant data of a process to calculate the risk score
    :type process_dict: Dict[str: Any]
    :return: Dict[str: Any]
    """

    print(metrics_dict)
