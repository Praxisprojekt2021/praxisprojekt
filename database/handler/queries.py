def get_process_list() -> str:
    """
    Function to get the cypher query to receive all processes

    :return: Query as string
    """
    return "Match (p: Process) " \
           "Return collect(properties(p))"


def get_process(uid: str) -> str:
    """
    Function to get the cypher query to receive a process

    :param uid: UID as a String
    :type uid: str
    :return: Query as string
    """
    # ToDo. Sobald man bei den Target_metrics anstatt dem Wert ein Dict mit drei Werten zurückgegeben bekommen möchte,
    # muss t.value durch properties(t) ersetzt werden
    return "Match (p: Process {uid: '" + uid + "'}) " \
            "Call {" \
            "With p " \
            "Optional Match (p)-[t:targets]-(m:Metric) " \
            "Return collect({value: t.value, metric: m.name}) As target_metrics" \
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


def update_process(uid: str, name: str, responsible_person: str, description: str, last_timestamp: str) -> str:
    """
    Function to get the cypher query to update a process

    :param uid: UID as a String
    :type uid: str
    :param name: name as a String
    :type name: str
    :param responsible_person: responsible_person as a String
    :type responsible_person: str
    :param description: description as a String
    :type description: str
    :param last_timestamp: last_timestamp as a String
    :type last_timestamp: str
    :return: Query as string
    """
    return "Match (p: Process {uid: '" + uid + "'}) " \
            "Optional Match (p)-[t:targets]-(m:Metric) " \
            "Delete t " \
            "Set p.name = '" + name + "' " \
            "Set p.responsible_person = '" + responsible_person + "' " \
            "Set p.description = '" + description + "' " \
            "Set p.last_timestamp = '" + last_timestamp + "' "


def update_process_metric(uid: str, name: str, value: float) -> str:
    """
    Function to get the cypher query to update a process metric

    :param uid: UID as a String
    :type uid: str
    :param name: name as a String
    :type name: str
    :param value: value of relation as a float
    :type value: float
    :return: Query as string
    """
    return "Match (p: Process {uid: '" + uid + "'}), (m: Metric {name: '" + name + "'}) " \
            "Create (p)-[t: targets {value: " + str(value) + "}]->(m)"


def delete_process(uid: str) -> str:
    """
    Function to get the cypher query to delete a process

    :param uid: UID as a String
    :type uid: str
    :return: Query as string
    """
    return "Match (p: Process {uid: '" + uid + "'}) " \
            "Detach Delete p"


def add_process_reference(process_uid: str, component_uid: str, weight: float):
    """
    Function to get the cypher query to add a process reference

    :param process_uid: process_uid as a String
    :type process_uid: str
    :param component_uid: component_uid as a String
    :type component_uid: str
    :param weight: weight as a float
    :type weight: float
    :return: Query as string
    """
    return f"Match (p: Process {{uid: '{process_uid}'}}), (c: Component {{uid: '{component_uid}'}}) " \
           f"Create (p)-[i: includes {{weight: {str(weight)}}}]->(c)"


def update_process_reference(uid: str, old_weight: float, new_weight: float):
    """
    Function to get the cypher query to add a process reference

    :param process_uid: process_uid as a String
    :type process_uid: str
    :param old_weight: old_weight as a float
    :type old_weight: float
    :param new_weight: new_weight as a float
    :type new_weight: float
    :return: Query as string
    """
    return f"Match (p: Process {{uid: '{uid}'}})-[i: includes {{weight: {old_weight}}}]-() " \
           f"Set i.weight={str(new_weight)}"


def delete_process_reference(uid: str, weight: float) -> str:
    """
    Function to get the cypher query to delete a process reference

    :param uid: UID as a String
    :type uid: str
    :param weight: weight as a float
    :type weight: float
    :return: Query as string
    """
    return "Match (n: Process {uid: '" + uid + "'})-[r: includes {weight: " + str(weight) + "}]-() Delete r"


def get_component_list() -> str:
    """
    Function to get the cypher query to get all components

    :return: Query as string
    """
    return "Match (c: Component) " \
           "Return collect(properties(c))"


def get_component(uid: str) -> str:
    """
    Function to get the cypher query to receive a component

    :param uid: UID as a String
    :type uid: str
    :return: Query as string
    """
    return "Match (c: Component {uid: '" + uid + "'}) " \
            "Call { " \
            "With c " \
            "Optional Match (c)-[h:has]-(m:Metric) " \
            "Return collect({value: h.value, metric: m.name}) As y " \
            "} " \
            "Return {properties: properties(c), metrics: y}"


def update_component(uid: str, name: str, category: str, description: str, last_timestamp: str) -> str:
    """
    Function to get the cypher query to update a component

    :param uid: UID as a String
    :type uid: str
    :param name: name as a String
    :type name: str
    :param category: category as a String
    :type category: str
    :param description: description as a String
    :type description: str
    :param last_timestamp: last_timestamp as a String
    :type last_timestamp: str
    :return: Query as string
    """
    return "Match (c: Component {uid: '" + uid + "'}) " \
            "Optional Match (c)-[r:has]-(m:Metric) " \
            "Delete r " \
            "Set c.name = '" + name + "' " \
            "Set c.category = '" + category + "' " \
            "Set c.description = '" + description + "' " \
            "Set c.last_timestamp = '" + last_timestamp + "' "


def update_component_metric(uid: str, name: str, value: float) -> str:
    """
    Function to get the cypher query to update a component metric

    :param uid: UID as a String
    :type uid: str
    :param name: name as a String
    :type name: str
    :param value: value of relation as a float
    :type value: float
    :return: Query as string
    """
    return "Match (c: Component {uid: '" + uid + "'}), (m: Metric {name: '" + name + "'}) " \
            "Create (c)-[r: has {value: " + str(value) + "}]->(m)"


def delete_component(uid: str) -> str:
    """
    Function to get the cypher query to delete a component

    :param uid: UID as a String
    :type uid: str
    :return: Query as string
    """
    return "Match (c: Component {uid: '" + uid + "'}) " \
            "Detach Delete c"


def get_metrics_list() -> str:
    """
    Function to get the cypher query to receive all Metrics

    :return: Query as string
    """
    return "Match (m: Metric) Return collect(properties(m))"
