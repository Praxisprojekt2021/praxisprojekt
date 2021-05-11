import unittest, json
from database.handler.metric_handler import create_from_frontend_json, get_metrics_data
from unittesting.database_handler.test_data_metric_handler import *
from neomodel import db

class getMetricsData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # add new metric
       create_from_frontend_json('unittesting/database_handler/test_data_create_from_frontend_json.json')

    def test_3003(self):
        data = get_metrics_data()

        with open('unittesting/database_handler/test_data_create_from_frontend_json.json') as json_file:
            data_json = json.load(json_file)

        result = True

        if 'Test' not in data['metrics']:
            result = False

        if result and data['metrics']['Test']['fulfilled_if'] != data_json['features']['code_quality']['metrics']['Test']['fulfilled_if']:
            result = False

        self.assertEqual(True, result)

    @classmethod
    def tearDownClass(cls):
        query = f"Match (m: Metric {{name: 'Test'}}) Detach Delete m"
        db.cypher_query(query)

class CreateFromFrontendJson(unittest.TestCase):

    def test_3001(self):
        data = 'frontend/static/content/mapping_metrics.json'
        self.assertRaises(FileNotFoundError, create_from_frontend_json, data)

    def test_3002(self):
        data = CREATE_FROM_FRONTEND_JSON
        self.assertRaises(TypeError, create_from_frontend_json, data)

if __name__ == '__main__':
    unittest.main()
