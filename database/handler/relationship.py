from neomodel import StructuredRel, FloatProperty


class Relationship(StructuredRel):
    """
    A class to represent the relationship between two nodes.

    Attributes
    ----------
    value : float
        is value of the relationship
    """

    value = FloatProperty()
