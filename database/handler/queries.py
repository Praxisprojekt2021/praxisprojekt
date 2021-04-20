def get_process_list() -> str:
    """
    Function to get the cypher query to receive all Processes

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
            "Optional Match (p)-[t:has]-(m:Metric) " \
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
    return "Match (p: Process {uid: '" + uid + "'}) " \
            "Optional Match (p)-[r:has]-(m:Metric) " \
            "Delete r " \
            "Set p.name = '" + name + "' " \
            "Set p.responsible_person = '" + responsible_person + "' " \
            "Set p.description = '" + description + "' " \
            "Set p.last_timestamp = '" + last_timestamp + "' "


def update_process_metric(uid: str, name: str, value: float) -> str:
    return "Match (p: Process {uid: '" + uid + "'}), (m: Metric {name: '" + name + "'}) " \
            "Create (p)-[r: has {value: " + str(value) + "}]->(m)"


def delete_process(uid: str) -> str:
    return "Match (p: Process {uid: '" + uid + "'}) " \
            "Detach Delete p"


def get_component_list() -> str:
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
    return "Match (c: Component {uid: '" + uid + "'}) " \
            "Optional Match (c)-[r:has]-(m:Metric) " \
            "Delete r " \
            "Set c.name = '" + name + "' " \
            "Set c.category = '" + category + "' " \
            "Set c.description = '" + description + "' " \
            "Set c.last_timestamp = '" + last_timestamp + "' "


def update_component_metric(uid: str, name: str, value: float) -> str:
    return "Match (c: Component {uid: '" + uid + "'}), (m: Metric {name: '" + name + "'}) " \
            "Create (c)-[r: has {value: " + str(value) + "}]->(m)"


def delete_component(uid: str) -> str:
    return "Match (c: Component {uid: '" + uid + "'}) " \
            "Detach Delete c"


def get_metrics_list() -> str:
    """
    Function to get the cypher query to receive all Metrics

    :return: Query as string
    """
    return "Match (m: Metric) Return collect(properties(m))"
