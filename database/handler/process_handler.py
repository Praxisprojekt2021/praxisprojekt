from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, StructuredRel, FloatProperty, relationship, db
from datetime import datetime

from core.success_handler import success_handler
from database.handler.relationship import Relationship
import database.handler.metric_handler as metric_handler
import database.handler.component_handler as component_handler
from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


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

    hasComponent = RelationshipTo(component_handler.Component, "includes", model=Relationship)
    hasMetric = RelationshipTo(metric_handler.Metric, "targets", model=Relationship)


def get_process_list() -> dict:
    """
    Function to retrieve a list of all processes

    :return: List of processes in a dict
    """

    processes = Process.nodes.all()
    processes_dict = success_handler()
    processes_dict["processes"] = []

    wanted_keys = ['uid', 'name', 'creation_timestamp', 'last_timestamp']
    for process in processes:
        process_dict = process.__dict__
        processes_dict["processes"].append(dict((k, process_dict[k]) for k in wanted_keys if k in process_dict))

    return processes_dict


def get_process(input_dict: dict) -> dict:
    """
    Function to retrieve a single process

    :param input_dict: process uid
    :type input_dict: dict
    :return: process dict
    """

    uid = input_dict["uid"]
    process = Process.nodes.get(uid=uid)
    process_dict = success_handler()
    process_dict["process"] = process.__dict__

    component_list = process.hasComponent.all()
    process_dict["process"]["components"] = []

    for component in component_list:
        component_dict = component_handler.get_component({"uid": component.uid})["component"]

        rel = process.hasComponent.relationship(component)
        component_dict["value"] = rel.value

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

    output = Process(
        name=input_dict["process"]["name"],
        creation_timestamp=str(datetime.now()),
        last_timestamp=str(datetime.now()),
        description=input_dict["process"]["description"])

    output.save()

    for metric in input_dict["target_metrics"]:
        output.hasMetric.connect(metric_handler.Metric.nodes.get(name=metric), {"value": input_dict["target_metrics"][metric]})

    data = success_handler()
    data["process_uid"] = output.uid

    return data


def update_process(input_dict: dict) -> dict:
    """
    Function to edit a single process

    :param input_dict: process as a dictionary
    :type input_dict: dict
    :return: Status dict
    """

    uid = input_dict["process"]["uid"]
    process = Process.nodes.get(uid=uid)
    process.name = input_dict["process"]["name"]
    process.description = input_dict["process"]["description"]
    process.last_timestamp = str(datetime.now())
    process.save()

    old_metrics = get_process({"uid": uid})["target_metrics"]
    new_metrics = input_dict["target_metrics"]

    for metric in old_metrics:
        metric_object = metric_handler.Metric.nodes.get(name=metric)
        if metric in new_metrics:
            rel = process.hasMetric.relationship(metric_object)
            rel.value = new_metrics[metric]
            rel.save()

            new_metrics.pop(metric)
        else:
            process.hasMetric.disconnect(metric_object)

    for metric in new_metrics:
        metric_object = metric_handler.Metric.nodes.get(name=metric)
        process.hasMetric.connect(metric_object, {"value": new_metrics[metric]})

    return success_handler()


def delete_process(input_dict: dict) -> dict:
    """
    Function to delete a single process

    :param input_dict: Identifier
    :type input_dict: dict
    :return: Status dict
    """

    Process.nodes.get(uid=input_dict["uid"]).delete()

    return success_handler()


def add_process_reference(input_dict: dict) -> dict:
    """
    Function to add a process reference (to a component included in the respective process)

    :param input_dict: a dictionary containing process uid, component id and value
    :type input_dict: dict
    :return: Status dict
    """

    process = Process.nodes.get(uid=input_dict['process_uid'])
    component = component_handler.Component.nodes.get(uid=input_dict['component_uid'])

    process.hasComponent.connect(component, {"value": input_dict["value"]})

    return success_handler()


def update_process_reference(input_dict: dict) -> dict:
    """
    Function to edit a process reference (to a component included in the respective process)

    :param input_dict: process uid and an old and new value
    :type input_dict: dict
    :return: Status dict
    """

    process = Process.nodes.get(uid=input_dict['uid'])

    component_list = process.hasComponent.all()

    for component in component_list:
        rel = process.hasComponent.relationship(component)
        if rel.value == input_dict['old_value']:
            rel.value = input_dict['new_value']
            rel.save()

    return success_handler()


def delete_process_reference(input_dict: dict) -> dict:
    """
    Function to delete a process reference (to a component not longer in the respective process)

    :param input_dict: a dictionary including the process uid and a value
    :type input_dict: dict
    :return: Status dict
    """

    db.cypher_query('Match (n: Process {uid: "' + input_dict['uid'] +
                    '"})-[r: includes {value: ' + str(input_dict['value']) + '}] -() Delete r')

    return success_handler()
