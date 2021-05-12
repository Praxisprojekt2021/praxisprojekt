from datetime import datetime

from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, relationship, db

import database.handler.metric_handler as metric_handler
import database.handler.queries as queries
import database.handler.reformatter as reformatter
from core.success_handler import success_handler
from database.config import *

from database.handler.relationships import RelationshipComponentMetric

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(
    NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Component(StructuredNode):
    """
    A class to represent a Component.

    Attributes
    ----------
    uid : str
        component id
    name : str
        name of the component
    category : str
        name of the component category
    description : str
        description of the component
    creation_timestamp : str
        timestamp of creation time
    last_timestamp : str
        timestamp of last update
    hasMetric : relationship
        relationship to metric
    """

    uid = UniqueIdProperty()
    name = StringProperty()
    category = StringProperty()
    description = StringProperty()
    creation_timestamp = StringProperty()
    last_timestamp = StringProperty()

    hasMetric = RelationshipTo(
        metric_handler.Metric, "has", model=RelationshipComponentMetric)


@db.transaction
def add_component(input_dict: dict) -> dict:
    """
    Function to add a single component

    :param input_dict: Component as a dictionary
    :type input_dict: dict
    :return: Status dict
    """

    output = Component(name=input_dict["name"], category=input_dict["category"],
                       creation_timestamp=str(datetime.now()),
                       last_timestamp=str(datetime.now()), description=input_dict["description"])

    output.save()

    for metric in input_dict["metrics"]:
        output.hasMetric.connect(metric_handler.Metric.nodes.get(
            name=metric), {"value": input_dict["metrics"][metric]})

    return success_handler()


def get_component_list() -> dict:
    """
    Function to retrieve a list of all existing components

    :return: List of components in a dict
    """
    output_dict = success_handler()

    query = queries.get_component_list()
    result, _ = db.cypher_query(query)
    output_dict["components"] = result[0][0]

    return output_dict


def get_component(input_dict: dict) -> dict:
    """
    Function to retrieve a single component

    :param input_dict: Component uid
    :type input_dict: dict
    :return: Component dict
    """
    output_dict = success_handler()

    result, _ = db.cypher_query(queries.get_component(input_dict["uid"]))
    output_dict["component"] = reformatter.reformat_component(result[0][0])

    return output_dict


def update_component(input_dict: dict) -> dict:
    """
    Function to update a single component

    :param input_dict: Component as a dictionary
    :type input_dict: dict
    :return: Status dict
    """
    uid = input_dict["uid"]

    query = queries.update_component(uid, input_dict["name"], input_dict["category"], input_dict["description"],
                                     str(datetime.now()))
    db.cypher_query(query)

    for metric in input_dict["metrics"]:
        query = queries.update_component_metric(
            uid, metric, input_dict["metrics"][metric])
        db.cypher_query(query)

    return success_handler()


def delete_component(input_dict: dict) -> dict:
    """
    Function to delete a single component

    :param input_dict: Identifier
    :type input_dict: dict
    :return: Status dict
    """

    query = queries.delete_component(input_dict["uid"])
    db.cypher_query(query)

    return success_handler()
