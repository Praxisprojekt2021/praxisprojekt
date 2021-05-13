import unittest
import json
from neomodel import db

from database.handler.metric_handler import Metric, create_from_frontend_json, get_metrics_data
from unittesting.test_database_handler.test_data_metric_handler import *


class TestGetMetricsData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # add new metric
        Metric.create({'name': 'test', "fulfilled_if": '>'})

    def test_3003_correct_execution(self):
        data = get_metrics_data()

        data['metrics']['test']['uid'] = ''

        self.assertEqual(data['metrics']['test'], GET_METRICS_DATA_OUT)

    @classmethod
    def tearDownClass(cls):
        query = "Match (m: Metric {name: 'test'}) Detach Delete m"
        db.cypher_query(query)


class CreateFromFrontendJson(unittest.TestCase):

    def test_3001_unknown_file(self):
        with self.assertRaises(FileNotFoundError):
            create_from_frontend_json('frontend/static/content/mapping_metrics.json')

    def test_3002_correct_input(self):
        create_from_frontend_json('test_database_handler/test_data_create_from_frontend_json.json')

        data = get_metrics_data()
        data['metrics']['test']['uid'] = ''

        self.assertEqual(data['metrics']['test'], GET_METRICS_DATA_OUT)

        query = "Match (m: Metric {name: 'test'}) Detach Delete m"
        db.cypher_query(query)


if __name__ == '__main__':
    unittest.main()
