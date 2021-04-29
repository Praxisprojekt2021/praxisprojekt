from neomodel import StructuredRel, FloatProperty


class RelationshipComponentMetric(StructuredRel):
    """
    A class to represent the relationship between a Component and a Metric.

    Attributes
    ----------
    value : float
        is value of the relationship
    """

    value = FloatProperty()


class RelationshipProcessComponent(StructuredRel):
    """
    A class to represent the relationship between a Process and a Component.

    Attributes
    ----------
    weight : float
        is the weight of the relationship
    """

    weight = FloatProperty()


class RelationshipProcessMetric(StructuredRel):
    """
    A class to represent the relationship between a Process and a Metric.

    Attributes
    ----------
    value : float
        is value of the relationship
    """

    average = FloatProperty()
    min = FloatProperty()
    max = FloatProperty()
