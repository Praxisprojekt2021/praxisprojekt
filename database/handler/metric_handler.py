from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty
import json

from core.success_handler import success_handler
from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Metric(StructuredNode):
    """
    A class to represent a Metric.

    Attributes
    ----------
    uid : str
        unique id of the metric
    name : str
        name of the metric
    fulfilled_if: str
        string containing whether the metric is fulfilled with a result > or < the result
   """

    uid = UniqueIdProperty()
    name = StringProperty()
    fulfilled_if = StringProperty()


def create_from_frontend_json(path: str) -> dict:
    """
    Function to create metrics out of the frontend definition file

    :param path: Path to stored json
    :type path: str
    :return: Stats dict
    """

    with open(path) as json_file:
        data = json.load(json_file)

    features = data["features"]

    for key in features:
        for metric in features[key]["metrics"]:
            for fulfill in features[key]["metrics"][metric]["fulfilled_if"]:
                Metric.create({'name': metric, "fulfilled_if": fulfill})

    return success_handler()


def get_metrics_data() -> dict:
    """
    Function to get all metrics and their attributes

    :return: Metrics dict
    """

    metrics = Metric.nodes.all()
    metrics_dict = success_handler()
    metrics_dict["metrics"] = []

    for metric in metrics:
        metric_dict = metric.__dict__
        metrics_dict["metrics"].append(metric_dict)

    return metrics_dict
