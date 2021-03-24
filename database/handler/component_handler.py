from datetime import datetime
from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, StructuredRel, FloatProperty

from core.error_handler import error_handler
from core.success_handler import success_handler
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
        name of the metric
    name : str
        name of the metric
    category : str
        name of the metric
    description : str
        name of the metric
    creation_timestamp : str
        description of the metric
    last_timestamp : str
        description of the metric
    hasMetric : relationship
        description of the metric
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
    component_dict.update({"success": True})

    return component_dict


def add_component(input_dict: dict) -> dict:
    """
    Function to add a single component

    :param input_dict: Component as a dictionary
    :type input_dict: dict
    :return: Status dict
    """
    successful = True

    output = Component(name=input_dict["name"], category=input_dict["category"],
                       creation_timestamp=str(datetime.now()),
                       last_timestamp=str(datetime.now()), description=input_dict["description"])
    try:
        output.save()
    except:  # since here can happen multiple errors we don't catch a explicit exception
        successful = False

    for metric in input_dict["metrics"]:
        try:
            output.hasMetric.connect(metric_handler.get_metric(metric), {"value": input_dict["metrics"][metric]})
        except:  # since here can happen multiple errors we don't catch a explicit exception
            successful = False

    if successful:
        return success_handler()
    else:
        return error_handler(500, "Unable to add component to database")


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

    successful = True

    try:
        component.save()
    except:  # since here can happen multiple errors we don't catch a explicit exception
        successful = False

    component_dict = get_component({"uid": uid})

    metrics_dict = component_dict["metrics"]
    metrics = []
    for key in metrics_dict:
        metrics.append(key)
    for metric in metrics:
        new_metrics = input_dict["metrics"]
        metric_object = metric_handler.get_metric(metric)
        rel = component.hasMetric.relationship(metric_object)
        rel.value = new_metrics[metric]
        try:
            rel.save()
        except:  # since here can happen multiple errors we don't catch a explicit exception
            successful = False

    if successful:
        return success_handler()
    else:
        return error_handler(500, "Unable to update component in database")


def delete_component(uid_dict: dict) -> dict:
    """
    Function to delete a single component

    :param uid_dict: Identifier
    :type uid_dict: dict
    :return: Status dict
    """
    if Component.nodes.get(uid=uid_dict["uid"]).delete():
        return success_handler()
    else:
        return error_handler(500, "Unable to delete component from database")
