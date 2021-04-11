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

    current_values = calculate_current_values(process_dict, metrics_dict)
    compared_values = compare_actual_target_metrics(current_values, metrics_dict)
    full_process_dict = calculate_risk_score(compared_values)

    return full_process_dict


def calculate_current_values(process_dict: dict, metrics_dict: dict) -> dict:
    """
    Function that extracts the current metrics values from a process dict

    :param process_dict: A dict containing all relevant data of a process to calculate the risk score
    :type process_dict: Dict[str: Any]
    :param metrics_dict: output from get_metrics_data()
    :type metrics_dict: dict
    :return: Dict[str: Any]
    """

    # get all metric values of components
    component_metrics = {}
    for components in (process_dict["process"]["components"]):
        for key, values in components["metrics"].items():
            if key not in component_metrics:
                component_metrics[key] = [values]
            else:
                component_metrics[key].append(values)

    # prepare output dict
    output_dict = {'success': process_dict["success"],
                   'process': process_dict["process"],
                   'actual_target_metrics': {}}

    # loop through all metrics
    for metric in metrics_dict['metrics']:
        calculations = {metric: {}}

        process_target_flag = False
        component_metric_flag = False

        # if any component has this specific metric
        if metric in component_metrics.keys():
            values = component_metrics[metric]

            # calculate actual metrics
            calculations[metric]['actual'] = {"total": sum(values), "min": min(values), "max": max(values),
                                              "average": mean(values)}

            # more than one component has this metric, thus a standard deviation can be calculated
            if len(values) > 1:
                calculations[metric]['actual'].update({"standard_deviation": stdev(values)})

            # only one component has this metric, thus no standard deviation can be calculated
            else:
                calculations[metric]['actual'].update({"standard_deviation": None})

            # get amount of components
            calculations[metric]["count_component"] = len(values)

            component_metric_flag = True

        # if process has a target value for this metric
        if metric in process_dict['target_metrics'].keys():
            value = process_dict['target_metrics'][metric]

            # calculate and get target metrics
            calculations[metric]['target'] = {'average': value}

            process_target_flag = True

        # if target values were given and the metric is filled in a component
        if process_target_flag and component_metric_flag:

            # calculate target sum
            calculations[metric]['target']['total'] = calculations[metric]['target']['average'] * \
                                                      calculations[metric]['count_component']

        # save calculated values in output_dict
        if process_target_flag or component_metric_flag:
            output_dict['actual_target_metrics'][metric] = calculations[metric]

    return output_dict


def compare_actual_target_metrics(process_dict: dict, metrics_dict: dict) -> dict:
    """
    Compares the actual value against the target value
    and sets the fulfillment to true or false based on
    the comparator of the related metric.

    :param process_dict: output from calculate_current_values()
    :type process_dict: dict
    :param metrics_dict: output from get_metrics_data()
    :type metrics_dict: dict
    :return: process_dict
    """

    for metric in process_dict['actual_target_metrics']:
        comparator = metrics_dict['metrics'][metric]['fulfilled_if']
        process_metrics_dict = process_dict['actual_target_metrics'][metric]

        # check if target and actual values are given
        if 'actual' in process_metrics_dict.keys() and 'target' in process_metrics_dict.keys():

            if eval(f"{process_metrics_dict['actual']['average']} {comparator}= {process_metrics_dict['target']['average']}"):

                fulfillment = True
            else:
                fulfillment = False

            process_dict['actual_target_metrics'][metric]['fulfillment'] = fulfillment

    return process_dict


def calculate_risk_score(process_dict: dict) -> dict:
    """
    Calculates the average fulfillment rate for
    all compared metrics

    :param process_dict: from compare_actual_target_metrics()
    :type process_dict: dict
    :return: process_dict
    """

    sum = 0
    amount = 0

    sub_dict = process_dict["actual_target_metrics"]
    for metric, values in sub_dict.items():
        if 'fulfillment' in values.keys():
            if values['fulfillment']:
                sum += 1
            amount += 1

    if amount > 0:
        score = int((sum / amount) * 100)
    else:
        score = None

    process_dict["score"] = score

    return process_dict
