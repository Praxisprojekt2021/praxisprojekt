def reformat_metric(input_dict: dict) -> dict:
    """
    Function to reformat a metric data from the neo4j database

    :param input_dict: Metric data
    :type input_dict: dict
    :return: Metric as a dict
    """
    output_dict = {input_dict["metric"]: input_dict["value"]}

    return output_dict


def reformat_component(input_dict: dict) -> dict:
    """
    Function to reformat a component data from the neo4j database

    :param input_dict: Component data
    :type input_dict: dict
    :return: Component as a dict
    """
    output_dict = input_dict["properties"]
    output_dict["metrics"] = {}

    for metric in input_dict["metrics"]:
        if metric["metric"] is None or metric["value"] is None:
            continue
        else:
            output_dict["metrics"].update(reformat_metric(metric))

    if "weight" in input_dict:
        output_dict["weight"] = input_dict["weight"]

    return output_dict


def reformat_process(input_dict: dict) -> (dict, dict):
    """
    Function to reformat a Process data from the neo4j database

    :param input_dict: Process data
    :type input_dict: dict
    :return: Process as a dict
    """

    process_dict = input_dict[0]

    process_dict["components"] = []
    for component in input_dict[1]:
        if component["weight"] is None or component["properties"] is None:
            continue
        else:
            process_dict["components"].append(reformat_component(component))

    targets_dict = {}
    for metric in input_dict[2]:
        if metric["metric"] is None or metric["value"] is None:
            continue
        else:
            targets_dict.update(reformat_metric(metric))

    return process_dict, targets_dict
