from typing import Dict
import sum_neo4j


def addition(summand1: float, summand2: float) -> Dict[str, float]:
    """
    Sums up two numbers and returns the result as dictionary

    :param summand1: The first summand to add
    :type summand1: float
    :param summand2: The second summand to add
    :type summand2: float
    :return: A dictionary with the key "sum" and the sum of both summands as value
    """
    sum_neo4j.into_db(summand1, summand2)
    return {"sum": sum_neo4j.from_db()}
