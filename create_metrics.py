import database.handler.metric_handler as mh
import database.handler.process_handler as ph
import database.handler.component_handler as ch

# print(mh.create_from_frontend_json('frontend/static/content/mapping_metrics_definition.json'))

import core.core as core


# ph.delete_process_reference({'uid': '153fd7899gfe40569c0c35b9b983c7be', 'weight': 9})
# ph.add_process_reference({'process_uid': '153fd7899gfe40569c0c35b9b983c7be', 'component_uid': '3f9eaad09a8948499ce2fc679552036e', 'weight': 11})

for process in ph.get_process_list()['process']:
    x = ph.get_process({'uid': process['uid']})
x = 1
