from statistics import mean, stdev


def start_calculate_risk(process_dict: dict, metrics_dict: dict) -> dict:
    """
    The entry function and handler for the risk calculations. The risk score is calculated and returned with all related
    values.

    :param metrics_dict: A dict containing all relevant data for the metrics
    :type metrics_dict: Dict[str: Any]
    :param process_dict: A dict containing all relevant data of a process to calculate the risk score
    :type process_dict: Dict[str: Any]
    :return: Dict[str: Any]
    """

    current_val = calculate_current_values(process_dict)


def calculate_current_values(process_dict: dict) -> dict:
    """
    Function that extracts the current metrics values from a process dict

   :param process_dict: A dict containing all relevant data of a process to calculate the risk score
   :type process_dict: Dict[str: Any]
   :return: Dict[str: Any]
   """

    metrics_dict = {}
    for components in (process_dict["process"]["components"]):
        for key, value in components["metrics"].items():
            if key not in metrics_dict:
                metrics_dict[key] = [value]
            else:
                metrics_dict[key].append(value)

    calculations = {}
    for key, value in metrics_dict.items():
        calculations[key] = {"sum": sum(value),
                             "min": min(value),
                             "max": max(value),
                             "avg": int(mean(value)),
                             "std_dev": int(stdev(value))
                             }

    return calculations
