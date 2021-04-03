from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, StructuredRel, FloatProperty, relationship, db

# import core
from core.success_handler import success_handler 

import database.handler.metric_handler as metric_handler
import database.handler.component_handler as component_handler
from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class RelationshipComponent(StructuredRel):
    """
    A class to represent the relationship between a Process and a Component.

    Attributes
    ----------
    weight : float
        is the weight of the relationship
    """

    weight = FloatProperty()


class RelationshipMetric(StructuredRel):
    """
    A class to represent the relationship between a Process and a Metric.

    Attributes
    ----------
    value : float
        is value of the relationship
    """

    value = FloatProperty()


class Process(StructuredNode):
    """
    A class to represent a Process.

    Attributes
    ----------
    uid : str
        process id
    name : str
        name of the process
    description : str
        description of the process
    creation_timestamp : str
        timestamp of creation time
    last_timestamp : str
        timestamp of last update
    includesComponent : relationship
        relationship to component
    hasMetric : relationship
        relationship to metric
    """

    uid = UniqueIdProperty()
    name = StringProperty()
    description = StringProperty()
    creation_timestamp = StringProperty()  # evtl. float
    last_timestamp = StringProperty()  # evtl. float

    hasComponent = RelationshipTo(component_handler.Component, "includes", model=RelationshipComponent)
    hasMetric = RelationshipTo(metric_handler.Metric, "has", model=RelationshipMetric)


def get_process_list() -> dict:
    """
    Function to retrieve a list of all processes

    :return: List of processes in a dict
    """

    data = {
        "success": True,
        "process": [
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Kunde anlegen",
                "creation_timestamp": "20210210...",
                "last_timestamp": "20200211..."
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Kunde löschen",
                "creation_timestamp": "20210209...",
                "last_timestamp": "20210210..."
            }
        ]
    }

    return data


def get_process(uid_dict: dict) -> dict:
    """
    Function to retrieve a single process

    :param uid_dict: process uid
    :type uid_dict: dict
    :return: process dict
    """

    uid = uid_dict["uid"]
    process = Process.nodes.get(uid=uid)
    process_dict = success_handler()
    process_dict["process"] = process.__dict__

    component_list = process.hasComponent.all()
    process_dict["process"]["components"] = []

    for component in component_list:
        component_dict = component_handler.get_component({"uid": component.uid})
        del component_dict["success"]
        process_dict["process"]["components"].append(component_dict)

    metrics_list = process.hasMetric.all()
    process_dict["target_metrics"] = {}

    for metric in metrics_list:
        rel = process.hasMetric.relationship(metric)
        process_dict["target_metrics"][metric.name] = rel.value

    del process_dict["process"]["hasComponent"]
    del process_dict["process"]["hasMetric"]
    del process_dict["process"]["id"]

    return process_dict


def add_process(input_dict: dict) -> dict:
    """
    Function to add a single process

    :param input_dict: process as a dictionary
    :type input_dict: dict
    :return: Status dict
    """
    data = {
        "success": True,
        "process_uid": "b141f94973a43cf8ee972e9dffc1b004"
    }

    return data


def update_process(input_dict: dict) -> dict:
    """
    Function to edit a single process

    :param input_dict: process as a dictionary
    :type input_dict: dict
    :return: Status dict
    """
    return success_handler()


def delete_process(uid_dict: dict) -> dict:
    """
    Function to delete a single process

    :param uid_dict: Identifier
    :type uid_dict: dict
    :return: Status dict
    """
    return success_handler()


def add_process_reference(input_dict: dict) -> dict:
    """
    Function to add a process reference/ add a process step

    :param input_dict: process id plus component id plus weight
    :type input_dict: dict
    :return: Status dict
    """

    process = Process.nodes.get(uid=input_dict['process_uid'])
    component = component_handler.Component.nodes.get(uid=input_dict['component_uid'])

    process.hasComponent.connect(component, {"weight": input_dict["weight"]})

    return success_handler()


def update_process_reference(input_dict: dict) -> dict:
    """
    Function to edit a process reference/ edit a process step

    :param input_dict: process id plus weights
    :type input_dict: dict
    :return: Status dict
    """

    process = Process.nodes.get(uid=input_dict['uid'])

    component_list = process.hasComponent.all()

    for component in component_list:
        rel = process.hasComponent.relationship(component)
        if rel.weight == input_dict['old_weight']:
            rel.weight = input_dict['new_weight']
            rel.save()

    return success_handler()


def delete_process_reference(input_dict: dict) -> dict:
    """
    Function to edit a process reference/ edit a process step

    :param input_dict: process id plus weight
    :type input_dict: dict
    :return: Status dict
    """

    db.cypher_query('Match (n: Process {uid: "' + input_dict['uid'] +
                    '"})-[r: includes {weight: ' + str(input_dict['weight']) + '}] -() Delete r')

    return success_handler()
