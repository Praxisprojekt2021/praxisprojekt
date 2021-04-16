import database.handler.metric_handler as mh
import database.handler.process_handler as ph
import database.handler.component_handler as ch

# print(mh.create_from_frontend_json('frontend/static/content/mapping_metrics_definition.json'))

import core.core as core


# ph.delete_process_reference({'uid': '153fd7899gfe40569c0c35b9b983c7be', 'weight': 9})
# ph.add_process_reference({'process_uid': '153fd7899gfe40569c0c35b9b983c7be', 'component_uid': '3f9eaad09a8948499ce2fc679552036e', 'weight': 11})

data = {
    "process": {
        "uid": "ed32602042f443f19d54fae59341b612",  # when -1 it indicates that it is a new process, anything else indicates its an update
        "name": "!Test mit leeren Feldern",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
    },
    "target_metrics": {
        "downtime": {
            "average": 223,
            "min": None,
            "max": None,
        },
        "restart": {
            "average": None,
            "min": None,
            "max": None,
        },
        # ...
    },
}


# core.get_process({"uid": "f1e0b9fb750446fea3df43e2ba17855e"})
# core.create_edit_process(data)
print(core.get_process({"uid": "ed32602042f443f19d54fae59341b612"}))
