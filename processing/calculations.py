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
    print("TEST")
    current_val = calculate_current_values(process_dict)


def calculate_current_values(process_dict: dict) -> dict:
    """
    Function that extracts the current metrics values from a process dict

   :param process_dict: A dict containing all relevant data of a process to calculate the risk score
   :type process_dict: Dict[str: Any]
   :return: Dict[str: Any]
   """

    # get all metric values
    component_metrics = {}
    for components in (process_dict["process"]["components"]):
        for key, value in components["metrics"].items():
            if key not in component_metrics:
                component_metrics[key] = [value]
            else:
                component_metrics[key].append(value)

    # prepare output dict
    output_dict = {'actual_target_metrics': {}}
    calculations = output_dict['actual_target_metrics']

    for key, value in component_metrics.items():
        calculations[key] = {}

        # calculate actual metrics
        calculations[key]['actual'] = {"total": sum(value),
                                       "min": min(value),
                                       "max": max(value),
                                       "avg": mean(value),
                                       }
        try:
            calculations[key]['actual'].update({"std_dev": stdev(value)})
        # TODO: wann wäre das der Fall?
        except ValueError:
            calculations[key]['actual'].update({"std_dev": None})

        # get amount of components
        calculations[key]["count_component"] = len(value)

        # calculate and get target metrics
        calculations[key]['target'] = {'avg': process_dict['target_metrics'][key],
                                       'total': process_dict['target_metrics'][key] * len(value)}

    return output_dict


def compare_actual_target_metrics(process_dict: dict, metrics_dict: dict) -> dict:
    # how to compare? -> Metrics Dict?
    # fullfillment ergänzen
    """Function that compares the actual_target_metrics against the target values

    Args:
        process_dict (Dict): A dict containing all relevant data of a 
        process to calculate the risk score
        list of components with metrics and also the target metrics

    Returns:
        Dict[str: Any]: key=Metric, values: actual, target, count of components have this metrics, fullfillment(bool)


    """
<<<<<<< HEAD


    pass
=======
    pass
>>>>>>> c00eda2106839152eaf651e9cc956e7888230c2a
