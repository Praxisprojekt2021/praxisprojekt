from neomodel import config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, JSONProperty, RelationshipTo, StructuredRel
from metric_handler import Metric
import metric_handler as mh
from datetime import datetime
# from database.config import *

NEO4J_IP = "35.192.106.131"
NEO4J_PORT = "7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "XcHUfUY8wMZb"

config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(NEO4J_USER, NEO4J_PASSWORD, NEO4J_IP, NEO4J_PORT)


class Relationship(StructuredRel):
    value = IntegerProperty()


class Component(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    category = StringProperty()
    creation_timestamp = StringProperty()
    last_timestamp = StringProperty()
    
    relationship = RelationshipTo(Metric, "has", model=Relationship)


def get_component_list():
    """
    TODO: von DB Team auszufüllen und umzusetzen
    :param input_dict:
    :return:
    """

    return Component.nodes.all()


def get_component(input_uid):
    """
    TODO: von DB Team auszufüllen und umzusetzen
    :param input_dict:
    :return:
    """

    return Component.nodes.get(uid=input_uid)


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
        
    output = Component(name=input_dict["name"], category=input_dict["category"], creation_timestamp=input_dict["creation_timestamp"], last_timestamp=input_dict["last_timestamp"]).save()
    
    for metric in input_dict["metrics"]:
        output.relationship.connect(mh.get_metric(metric), {"value": input_dict["metrics"][metric]})

    return output


def update_component(input_dict):
    """
    TODO: von DB Team auszufüllen und umzusetzen
    :param input_dict:
    :return:
    """

    output = get_component(input_dict["uid"])
    
    output.name = input_dict["name"]
    output.category = input_dict["category"]
    output.last_timestamp = str(datetime.now())
    
    for metric in Metric.nodes.all():
        test = True
        for input in input_dict["metrics"]:
            if input == metric.name:
                if bool(output.relationship.relationship(mh.get_metric(metric.name))):
                    rel = output.relationship.relationship(mh.get_metric(input))
                    rel.value = input_dict["metrics"][input]
                    rel.save()
                    test = False
                else:
                    output.relationship.connect(mh.get_metric(input), {"value": input_dict["metrics"][input]})
                    test = False
        if test and bool(output.relationship.relationship(mh.get_metric(metric.name))):
            test = False  # delete relationship is not possible
    
    return output.save()


def delete_component(input_uid):
    return Component.nodes.get(uid=input_uid).delete()


# Zum Testen
data = {
    "uid": "635a37bfed344cd0b335d7da16711f4f",
    "name": "Programm2",
    "category": "Feature2",
    "last_timestamp": str(datetime.now()),
    "metrics": {
        "codelines": 50
    }
}

# print(add_component(data))
# print(update_component(data))
# print(get_component_list())
# print(delete_component(data["uid"]))
