from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, relationship, db
from datetime import datetime

from core.success_handler import success_handler
from database.handler.relationship import RelationshipProcessComponent, RelationshipProcessMetric
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

    hasComponent = RelationshipTo(component_handler.Component, "includes", model=RelationshipProcessComponent)
    hasMetric = RelationshipTo(metric_handler.Metric, "targets", model=RelationshipProcessMetric)


def get_process_list() -> dict:
    """
    Function to retrieve a list of all processes

    :return: List of processes in a dict
    """

    # get data from neo4j database
    processes = Process.nodes.all()

    output_dict = success_handler()
    processes_list = []

    for process in processes:
        process_dict = process.__dict__
        del process_dict["hasMetric"]
        del process_dict["description"]
        del process_dict["hasComponent"]
        processes_list.append(process_dict)

    output_dict["process"] = processes_list

    return output_dict


def get_process(input_dict: dict) -> dict:
    """
    Function to retrieve a single process

    :param input_dict: process uid
    :type input_dict: dict
    :return: process dict
    """

    # get data from neo4j database
    uid = input_dict["uid"]
    process_data = Process.nodes.get(uid=uid)
    component_nodes = process_data.hasComponent.all()
    metrics_list = process_data.hasMetric.all()

    # prepare general process data
    output_dict = success_handler()
    process_dict = process_data.__dict__

    del process_dict["hasComponent"]
    del process_dict["hasMetric"]
    del process_dict["id"]

    # prepare component data
    component_list = []

    for component in component_nodes:
        component_dict = component_handler.get_component({"uid": component.uid})["component"]

        rel = process_data.hasComponent.relationship(component)
        component_dict["weight"] = rel.weight

        component_list.append(component_dict)

    process_dict["components"] = component_list
    output_dict["process"] = process_dict

    # prepare metric data
    metrics_dict = {}

    for metric in metrics_list:
        rel = process_data.hasMetric.relationship(metric)
        metrics_dict[metric.name] = rel.value

    output_dict["target_metrics"] = metrics_dict

    return output_dict


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
        output.hasMetric.connect(metric_handler.get_metric(name=metric), {"value": input_dict["target_metrics"][metric]})

    output_dict = success_handler()
    output_dict["process_uid"] = output.uid

    return output_dict


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

    :param input_dict: a dictionary containing process uid, component id and weight
    :type input_dict: dict
    :return: Status dict
    """

    process = Process.nodes.get(uid=input_dict['process_uid'])
    component = component_handler.Component.nodes.get(uid=input_dict['component_uid'])

    process.hasComponent.connect(component, {"weight": input_dict["weight"]})

    return success_handler()


def update_process_reference(input_dict: dict) -> dict:
    """
    Function to edit a process reference (to a component included in the respective process)

    :param input_dict: process uid and an old and new weight
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
    Function to delete a process reference (to a component not longer in the respective process)

    :param input_dict: a dictionary including the process uid and a weight
    :type input_dict: dict
    :return: Status dict
    """

    db.cypher_query('Match (n: Process {uid: "' + input_dict['uid'] +
                    '"})-[r: includes {weight: ' + str(input_dict['weight']) + '}] -() Delete r')

    return success_handler()
