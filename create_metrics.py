from database.handler.metric_handler import create_from_frontend_json, create_from_csv, get_metrics_data
import core.core as core

# create_from_frontend_json('frontend/static/content/mapping_metrics_definition.json')
# create_from_csv('database/metrics.csv')


#print(get_metrics_data())
print(core.get_process(12))
