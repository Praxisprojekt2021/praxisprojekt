def get_process(uid: str) -> str:
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


def get_component(uid: str) -> str:
    return "Match (c: Component {uid: '" + uid + "'})" \
                                                 "Call {" \
                                                 "With c " \
                                                 "Optional Match (c)-[h:has]-(m:Metric)" \
                                                 "Return collect({value: h.value, metric: m.name}) As y" \
                                                 "}" \
                                                 "Return {properties: properties(c), metrics: y}"


def get_metrics_list() -> str:
    return "Match (m: Metric) Return collect(properties(m))"
