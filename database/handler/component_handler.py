from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, StructuredRel, FloatProperty
from datetime import datetime

from core.success_handler import success_handler
from database.handler.relationship import Relationship
import database.handler.metric_handler as metric_handler
from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


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
    creation_timestamp = StringProperty()  # evtl. float
    last_timestamp = StringProperty()  # evtl. float

    hasMetric = RelationshipTo(metric_handler.Metric, "has", model=Relationship)


def get_component_list() -> dict:
    """
    Function to retrieve a list of all existing components

    :return: List of components in a dict
    """

    components = Component.nodes.all()
    components_dict = success_handler()
    components_dict["components"] = []

    for component in components:
        component_dict = component.__dict__
        del component_dict["hasMetric"]
        del component_dict["description"]
        components_dict["components"].append(component_dict)

    return components_dict


def get_component(uid_dict: dict) -> dict:
    """
    Function to retrieve a single component

    :param uid_dict: Component uid
    :type uid_dict: dict
    :return: Component dict
    """

    uid = uid_dict["uid"]
    component = Component.nodes.get(uid=uid)
    component_dict = success_handler()
    component_dict["component"] = component.__dict__

    metrics_list = component.hasMetric.all()
    component_dict["component"]["metrics"] = {}

    for key in metrics_list:
        relationship = component.hasMetric.relationship(key)
        component_dict["component"]["metrics"][key.name] = relationship.value

    del component_dict["component"]["hasMetric"]
    del component_dict["component"]["id"]

    return component_dict


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
        output.hasMetric.connect(metric_handler.Metric.nodes.get(name=metric), {"value": input_dict["metrics"][metric]})

    return success_handler()


def update_component(input_dict: dict) -> dict:
    """
    Function to update a single component

    :param input_dict: Component as a dictionary
    :type input_dict: dict
    :return: Status dict
    """

    uid = input_dict["uid"]
    component = Component.nodes.get(uid=uid)
    component.name = input_dict["name"]
    component.description = input_dict["description"]
    component.category = input_dict["category"]
    component.last_timestamp = str(datetime.now())

    component.save()

    component_dict = get_component({"uid": uid})

    for metric in component_dict["component"]["metrics"]:
        new_metrics = input_dict["metrics"]
        metric_object = metric_handler.Metric.nodes.get(name=metric)
        rel = component.hasMetric.relationship(metric_object)
        rel.value = new_metrics[metric]
        rel.save()

    return success_handler()


def delete_component(input_dict: dict) -> dict:
    """
    Function to delete a single component

    :param input_dict: Identifier
    :type input_dict: dict
    :return: Status dict
    """

    uid = input_dict["uid"]
    Component.nodes.get(uid=uid).delete()

    return success_handler()
