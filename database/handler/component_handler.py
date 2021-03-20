from neomodel import config, StructuredNode, StringProperty, UniqueIdProperty, DateTimeProperty, db
from datetime import datetime

NEO4J_IP = "35.192.106.131"
NEO4J_PORT = "7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "XcHUfUY8wMZb"

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Component(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    category = StringProperty()
    creation_timestamp = DateTimeProperty(default_now=True)  # subject to change
    last_timestamp = DateTimeProperty(default_now=True)  # subject to change


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
    
    return Component.nodes.get(uid=input_dict["uid"])


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
    
    with db.transaction:
        new_component = Component(name=input_dict["name"], category=input_dict["category"]).save()
        return new_component


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


''' Zum Testen:
data = {
    "name": "aaron",
    "category": "jonathan"
}

x = add_component(data)
print(x)

print(get_component({"uid": x.uid}))
'''
