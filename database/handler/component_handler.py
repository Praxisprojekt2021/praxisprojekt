from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, DateTimeProperty

from database.config import *

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Component(StructuredNode):

    id = UniqueIdProperty()
    name = StringProperty()
    category = StringProperty()
    creation_timestamp = DateTimeProperty()
    last_timestamp = DateTimeProperty()


def get_component_list(input_dict):
    """
    TODO: von DB Team auszufüllen und umzusetzen

    :param input_dict:
    :return:
    """

    data = {
        "success": True,
        "components": [
            {"id": 1,
             "name": "SQL Datenbank",
             "category": "Datenbank",
             "creation_timestamp": "2020-02-04 07:46:29.315237",
             "last_timestamp": "2020-02-04 07:46:29.315237",
             },
            {"id": 2,
             "name": "Oracle Datenbank",
             "category": "Datenbank",
             "creation_timestamp": "2020-02-04 07:46:29.315237",
             "last_timestamp": "2020-02-04 07:46:29.315237",
             }
        ]
    }

    return data


def get_component(input_dict):
    """
    TODO: von DB Team auszufüllen und umzusetzen

    :param input_dict:
    :return:
    """

    data = {
        "success": True,
        "id": 1,
        "name": "SQL Datenbank",
        "category": "Datenbank",
        "description": "Datenbank zu xy mit ...",
        "creation_timestamp": "2020-02-04 07:46:29.315237",
        "last_timestamp": "2020-02-04 07:46:29.315237",
        "metrics": {
            "codelines": 20000,
            "admins": 10,
            "recovery_time": 5,
        },
    }

    return data


def add_component(input_dict):
    """
    TODO: von DB Team auszufüllen und umzusetzen

    :param input_dict:
    :return:
    id = UniqueIdProperty()
    name = StringProperty()
    category = StringProperty()
    creation_timestamp = DateTimeProperty()
    last_timestamp = DateTimeProperty()
    """
    new_component = Component(name=input_dict.name, category=input_dict.category)
    print(new_component.save())
    if new_component.refresh():
        print(True)
    """
    data = {
        "success": True,
    }

    return data
"""

def update_component(input_dict):
    """
    TODO: von DB Team auszufüllen und umzusetzen

    :param input_dict:
    :return:
    """

    data = {
        "success": True,
    }

    return data


def delete_component(input_dict):
    """
    TODO: von DB Team auszufüllen und umzusetzen

    :param input_dict:
    :return:
    """

    data = {
        "success": True,
    }

    return data
