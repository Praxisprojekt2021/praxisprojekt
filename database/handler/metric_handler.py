import csv
import json
from typing import Dict

from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty

from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Metric(StructuredNode):
    """
    A class to represent a Metric.

    Attributes
    ----------
    name : str
        name of the metric
    uid : str
        unique id of the metric
   """

    uid = UniqueIdProperty()
    name = StringProperty()


def create_from_csv(path: str):
    """
    Function to create metrics out of an csv file

    :param path: Path to the csv file
    :type path: int
    """

    with open(path) as csv_file:
        csv_reader_object = csv.reader(csv_file)

    for row in csv_reader_object:
        print(row)
        Metric.create({'name': row[0]})
    print(Metric.nodes.all())


def create_from_frontend_json(path: str):
    """
    Function to create metrics out of the frontend definition file
    """
    with open(path) as json_file:
        data = json.load(json_file)

    features = data["features"]

    for key in features:
        feature = features[key]
        metrics = feature["metrics"]
        for metric in metrics:
            Metric.create({'name': metric})


def get_metric(input_name: str) -> Metric:
    """
    Function to get metrics by its name

    :param input_name: Name of the metric
    :type input_name: str
    """
    return Metric.nodes.get(name=input_name)


def get_metrics_data() -> Dict:
    """
    Function to get metrics by its name

    """

    metrics = Metric.nodes.all()
    metrics_data_dict = {"sucess": True}

    for metric in metrics:
        metric_dict = metric.__dict__
        metric_name = metric_dict.pop('name')
        metrics_data_dict[metric_name] = metric_dict

        # TODO: delete the following two codelines
        metrics_data_dict[metric_name]["compared_to_target"] = ">"  # oder "<"
        metrics_data_dict[metric_name]["calculation_total"] = "sum"  # oder "product"

    return metrics_data_dict


def add_metric(input_dict: dict) -> Metric:
    """
    Function to create metric

    :param input_dict: Metric dict
    :type input_dict: dict
    """
    return Metric(name=input_dict["name"], description=input_dict["description"]).save()
