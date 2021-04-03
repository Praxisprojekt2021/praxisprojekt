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

    component_metrics = {}
    for components in (process_dict["process"]["components"]):
        for key, value in components["metrics"].items():
            if key not in component_metrics:
                component_metrics[key] = [value]
            else:
                component_metrics[key].append(value)

    calculations = {}
    for key, value in component_metrics.items():
        calculations[key] = {"sum": sum(value),
                             "min": min(value),
                             "max": max(value),
                             "avg": int(mean(value))
                             }
        try:
            calculations[key].update({"std_dev": int(stdev(value))})
        except ValueError:
            calculations[key].update({"std_dev": None})

    return calculations

def compare_actual_target_metrics(process_dict: dict) -> dict:
    """Function that compares the actual_target_metrics against the target values

    Args:
        process_dict (Dict): A dict containing all relevant data of a 
        process to calculate the risk score

    Returns:
        Dict[str: Any]
    """
    pass