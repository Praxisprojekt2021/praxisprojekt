from datetime import datetime
from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, StructuredRel, FloatProperty

import core.success_handler
import database.handler.metric_handler as metric_handler
from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Relationship(StructuredRel):
    """
    A class to represent the relationship between a Component and a Metric.

    Attributes
    ----------
    value : float
        is value of the relationship
    """
    value = FloatProperty()


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
    data = {"success": True}
    components = Component.nodes.all()
    components_list = []
    for component in components:
        component_dict = component.__dict__
        del component_dict["hasMetric"]
        components_list.append(component_dict)

    data["components"] = components_list
    return data


def get_component(uid_dict: dict) -> dict:
    """
    Function to retrieve a single component

    :param uid_dict: Component uid
    :type uid_dict: dict
    :return: Component dict
    """

    uid = uid_dict["uid"]
    component = Component.nodes.get(uid=uid)
    component_dict = component.__dict__

    metrics_list = component.hasMetric.all()
    metrics_dict = {}
    for key in metrics_list:
        relationship = component.hasMetric.relationship(key)
        metrics_dict[key.name] = relationship.value
    component_dict["metrics"] = metrics_dict

    del component_dict["hasMetric"]
    del component_dict["id"]
    component_dict.update(core.success_handler())

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
        output.hasMetric.connect(metric_handler.get_metric(metric), {"value": input_dict["metrics"][metric]})

    return core.success_handler()


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

    metrics = []
    for key in input_dict["metrics"]:
        metrics.append(key)
    for metric in metrics:
        new_metrics = input_dict["metrics"]
        metric_object = metric_handler.get_metric(metric)
        rel = component.hasMetric.relationship(metric_object)
        rel.value = new_metrics[metric]
        rel.save()

    return core.success_handler()


def delete_component(uid_dict: dict) -> dict:
    """
    Function to delete a single component

    :param uid_dict: Identifier
    :type uid_dict: dict
    :return: Status dict
    """
    Component.nodes.get(uid=uid_dict["uid"]).delete()
    return core.success_handler()
