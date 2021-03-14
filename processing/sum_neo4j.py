from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, FloatProperty,
                      RelationshipTo)
import configparser
from typing import Dict


class Sum(StructuredNode):
    value = FloatProperty()


value1 = 2.0
value2 = 3.2


def init_db():
    parser = configparser.ConfigParser()
    # REPLACE PATH
    parser.read_file(open(r'C:\Users\aaron\PycharmProjects\praxisprojekt\processing\config.txt'))
    config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(parser.get('neo4j', 'user'), parser.get('neo4j', 'password'),
                                                      parser.get('neo4j', 'ip'), parser.get('neo4j', 'port')).replace(
        '"',
        '')


def into_db(summand1: float, summand2: float):
    init_db()
    sum_node = Sum(value=(summand1 + summand2)).save()
    print("Saved {}".format(sum_node))


def from_db():
    init_db()
    accum = 0.0
    for sum_node in Sum.nodes:
        accum += sum_node.value
    return accum
