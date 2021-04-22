def get_process(uid: str) -> str:
    """
    Function get the cypher query to receive a process

    :param uid: UID as a String
    :type uid: str
    :return: Query as string
    """
    return "Match (p: Process {uid: '" + uid + "'}) " \
                                              "Call {" \
                                              "With p " \
                                              "Optional Match (p)-[t:has]-(m:Metric) " \
                                              "Return collect({value: properties(t), metric: m.name}) As target_metrics" \
                                              "} " \
                                              "Call {" \
                                              "With p " \
                                              "Optional Match (p)-[i:includes]-(c:Component) " \
                                              "Call {" \
                                              "With c " \
                                              "Optional Match (c)-[h:has]-(n:Metric) " \
                                              "Return collect({value: h.value, metric: n.name}) As y" \
                                              "}" \
                                              "Return collect({weight: i.weight, properties: properties(c), metrics: y}) As components" \
                                              "}" \
                                              "Return properties(p) As process, components, target_metrics"


def get_component(uid: str) -> str:
    """
    Function get the cypher query to receive a component

    :param uid: UID as a String
    :type uid: str
    :return: Query as string
    """
    return "Match (c: Component {uid: '" + uid + "'})" \
                                                 "Call {" \
                                                 "With c " \
                                                 "Optional Match (c)-[h:has]-(m:Metric)" \
                                                 "Return collect({value: h.value, metric: m.name}) As y" \
                                                 "}" \
                                                 "Return {properties: properties(c), metrics: y}"


def get_metrics_list() -> str:
    """
    Function get the cypher query to receive all Metrics

    :return: Query as string
    """
    return "Match (m: Metric) Return collect(properties(m))"
