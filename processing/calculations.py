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

    # prepare output dict
    output_dict = {'success': process_dict["success"],
                   'process': process_dict["process"],
                   'actual_target_metrics': {}}

    component_metrics = get_all_component_metrics(process_dict)
    target_metrics = get_all_target_metrics(process_dict)

    actual_target_values = calculate_current_values(
        metrics_dict, component_metrics, target_metrics)
    output_dict['actual_target_metrics'] = actual_target_values

    output_dict = compare_actual_target_metrics(output_dict, metrics_dict)
    output_dict = calculate_risk_score(output_dict)

    return output_dict


def get_all_component_metrics(process_dict):
    # get all metric values of components
    component_metrics = {}
    for components in (process_dict["process"]["components"]):
        for key, values in components["metrics"].items():
            if key not in component_metrics:
                component_metrics[key] = [values]
            else:
                component_metrics[key].append(values)

    return component_metrics


def get_all_target_metrics(process_dict):
    target_metrics = {}
    for metric, values in process_dict['target_metrics'].items():

        target_metrics[metric] = {}
        # calculate and get target metrics
        if "average" not in values:
            values["average"] = None
        if "min" not in values:
            values["min"] = None
        if "max" not in values:
            values["max"] = None
        target_metrics[metric]['target'] = {
            'average': values["average"], 'min': values["min"], 'max': values["max"]}

    return target_metrics


def calculate_current_values(metrics_dict: dict, component_metrics, target_metrics) -> dict:
    """
    Function that extracts the current metrics values from a process dict

    :param target_metrics:
    :type target_metrics:
    :param component_metrics:
    :type component_metrics:
    :param metrics_dict: output from get_metrics_data()
    :type metrics_dict: dict
    :return: Dict[str: Any]
    """

    actual_target_values = {}

    # loop through all metrics
    for metric in metrics_dict['metrics']:
        calculations = {metric: {}}

        process_target_flag = False
        component_metric_flag = False

        # if any component has this specific metric
        if metric in component_metrics.keys():
            calculations[metric] = calculate_actual_values(
                component_metrics[metric])
            component_metric_flag = True

        # if process has a target value for this metric
        if metric in target_metrics.keys():
            calculations[metric]['target'] = target_metrics[metric]['target']
            process_target_flag = True

        # if target values were given and the metric is filled in a component
        if process_target_flag and component_metric_flag:
            if calculations[metric]['target']['average'] is not None:
                # calculate target sum
                calculations[metric]['target']['total'] = calculations[metric]['target']['average'] * \
                                                          calculations[metric]['count_component']
        # save calculated values in output_dict
        if process_target_flag or component_metric_flag:
            actual_target_values[metric] = calculations[metric]

    return actual_target_values


def calculate_actual_values(actual_component_metric_data):
    """
    Calculates the actual values for one metric
    """

    actual_process_metric_data = {}

    # calculate actual metrics
    actual_process_metric_data['actual'] = {"total": sum(actual_component_metric_data),
                                            "min": min(actual_component_metric_data),
                                            "max": max(actual_component_metric_data),
                                            "average": mean(actual_component_metric_data)}

    # more than one component has this metric, thus a standard deviation can be calculated
    if len(actual_component_metric_data) > 1:
        actual_process_metric_data['actual'].update(
            {"standard_deviation": stdev(actual_component_metric_data)})

    # only one component has this metric, thus no standard deviation can be calculated
    else:
        actual_process_metric_data['actual'].update(
            {"standard_deviation": None})

    # get amount of components
    actual_process_metric_data["count_component"] = len(
        actual_component_metric_data)

    return actual_process_metric_data


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

            fulfillment = True
            # if eval(f"{process_metrics_dict['actual']['average']} {comparator}= {process_metrics_dict['target'][
            # 'average']}"):
            if process_metrics_dict['target']['min'] is not None:
                if process_metrics_dict['actual']['min'] < process_metrics_dict['target']['min']:
                    fulfillment = False

            if (process_metrics_dict['target']['max'] is not None) and fulfillment:
                if process_metrics_dict['actual']['max'] > process_metrics_dict['target']['max']:
                    fulfillment = False

            if (process_metrics_dict['target']['average'] is not None) and fulfillment:
                if not eval(
                        f"{process_metrics_dict['actual']['average']} {comparator}= {process_metrics_dict['target']['average']}"):
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
    for _, values in sub_dict.items():
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
