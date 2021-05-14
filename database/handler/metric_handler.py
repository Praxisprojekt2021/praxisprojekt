from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, db
import json

from core.success_handler import success_handler
import database.handler.queries as queries
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

    query = queries.get_metrics_list()
    result, meta = db.cypher_query(query)

    output_dict = success_handler()
    output_dict["metrics"] = {}

    for metric in result[0][0]:
        output_dict["metrics"][metric.pop('name')] = metric

    return output_dict


def set_metrics_unique_constraint() -> dict:
    """
    Function to set unique constraint on metric names

    :return: success handler
    """

    query = queries.set_metrics_unique_constraint()
    db.cypher_query(query)

    return success_handler()


def remove_metrics_unique_constraint() -> dict:
    """
    Function to remove unique constraint on metric names

    :return: success handler
    """

    query = queries.remove_metrics_unique_constraint()
    db.cypher_query(query)

    return success_handler()
