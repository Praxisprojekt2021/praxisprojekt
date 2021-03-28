from database.handler.metric_handler import create_from_frontend_json, create_from_csv

# create_from_frontend_json('docu/mapping_metrics_definition.json')
create_from_csv('database/metrics.csv')
