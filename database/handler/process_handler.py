from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, \
    RelationshipTo, StructuredRel, FloatProperty

import core

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
    A class to represent the relationship between a Component and a Metric.

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

    includesComponent = RelationshipTo(component_handler.Component, "includes", model=RelationshipComponent)
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
                "creation_timestamp": "2021-03-29 12:02:52.897594",
                "last_timestamp": "2021-03-29 12:02:52.897594"
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Kunde löschen",
                "creation_timestamp": "2021-03-29 12:02:52.897594",
                "last_timestamp": "2021-03-29 12:02:52.897594"
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

    data = {
        "success": True,
        "process": {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde anlegen",
            "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            "components": [
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
                    "weight": 1,  # different from single component view!
                    "name": "SQL Datenbank",
                    "category": "Datenbank",
                    "description": "Kundendatenbank",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "codelines": 20000,
                        "admins": 10,
                        "recovery_time": 5
                    }
                },
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
                    "weight": 1.5,
                    "name": "Frontend API",
                    "category": "API",
                    "description": "API für das Frontend",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "codelines": 20000,
                        "admins": 10,
                        "recovery_time": 5
                    }
                },
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
                    "weight": 2,
                    "name": "Hadoop Cluster",
                    "category": "Datenbank",
                    "description": "Big Data Plattform",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "codelines": 20000,
                        "admins": 10,
                        "recovery_time": 5
                    }
                }
            ]
        },
        "target_metrics": {
            "codelines": 25000,
            "admins": 12,
            "recovery_time": 3
        }
    }

    return data


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
    return core.success_handler()


def delete_process(uid_dict: dict) -> dict:
    """
    Function to delete a single process

    :param uid_dict: Identifier
    :type uid_dict: dict
    :return: Status dict
    """
    return core.success_handler()


def add_process_reference(input_dict: dict) -> dict:
    """
    Function to add a process reference/ add a process step

    :param input_dict: process is plus component id plus weight
    :type input_dict: dict
    :return: Status dict
    """
    return core.success_handler()


def update_process_reference(input_dict: dict) -> dict:
    """
    Function to edit a process reference/ edit a process step

    :param input_dict: process id plus weights
    :type input_dict: dict
    :return: Status dict
    """
    return core.success_handler()


def delete_process_reference(input_dict: dict) -> dict:
    """
    Function to edit a process reference/ edit a process step

    :param input_dict: process id plus weight
    :type input_dict: dict
    :return: Status dict
    """

    return core.success_handler()
