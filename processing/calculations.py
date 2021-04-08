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
    # print("TEST")
    current_val = calculate_current_values(process_dict)
    compared_vals = compare_actual_target_metrics(current_val, metrics_dict)
    full_process_dict = calculate_risk_score(compared_vals)

    return full_process_dict


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
    output_dict = {'success': process_dict["success"],
                   'process': process_dict["process"],
                   'actual_target_metrics': {}}

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


def compare_actual_target_metrics(process_dict: dict,
                                  metrics_dict: dict) -> dict:
    """Compares the actual value against the target value
        and sets the fulfillment to true or false based on
        the comparator of the related metric.

        :param process_dict: output from calculate_current_values()
        :type process_dict: dict
        :param metrics_dict: output from get_metrics_data()
        :type metrics_dict: dict
        :return: process_dict
    """
    for metric in process_dict['actual_target_metrics']:
        comparator = metrics_dict[metric]['fulfilled_if']

        if eval(f"{metric['actual']['avg']} {comparator}"
                f"{process_dict['target_metrics'][metric]}"):

            fulfillment = True
        else:
            fulfillment = False

        process_dict['actual_target_metrics'][metric]['fulfillment'] = fulfillment

    return process_dict


def calculate_risk_score(process_dict: dict) -> dict:
    """Calculates the average fulfillment rate for 
       all compared metrics

        :param process_dict: from compare_actual_target_metrics()
        :type process_dict: dict
        :return: process_dict
    """

    sum = 0
    sub_dict = process_dict["actual_target_metrics"]
    for metric in sub_dict:
        sum += sub_dict[metric]["fulfillment"]

    process_dict["score"] = int((sum/len(sub_dict))*100)

    return process_dict
