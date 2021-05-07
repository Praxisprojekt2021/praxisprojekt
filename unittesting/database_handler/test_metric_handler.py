import unittest
from database.handler.metric_handler import create_from_frontend_json


class Test_metric_handler(unittest.TestCase):

    def test_3001(self):
        data = "abc"
        self.assertRaises(FileNotFoundError, create_from_frontend_json, data)

    def test_3002(self):
        data = {
            'success': True,
            'metrics': {
                'automation': {
                    'uid': 'd0cfbd93a0d146d9a223b7cfad098a7a',
                    'fulfilled_if': '>'
                },
                'test_automation': {
                    'uid': '1de621af9cb7404291a55671463b5ad7',
                    'fulfilled_if': '>'
                },
            }
        }
        self.assertRaises(TypeError, create_from_frontend_json, data)


if __name__ == '__main__':
    unittest.main()
