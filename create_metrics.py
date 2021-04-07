from database.handler.metric_handler import create_from_frontend_json
import database.handler.process_handler as ph

# create_from_frontend_json('frontend/static/content/mapping_metrics_definition.json')

data = {
    "process": {"uid": "bfdef08a9dc54e1e9e34eb03ab41c028", "name": "xy", "description": "Test der Prozess_anlegen Funktion"},
    "target_metrics": {"comment_quality": 30, "external_support": 40, "downtime": 20}}

# print(ph.add_process(data))
# print(ph.update_process(data))
# print(ph.delete_process({"uid": "888e123ce5454a9aaf6dc1bb1d190513"}))
