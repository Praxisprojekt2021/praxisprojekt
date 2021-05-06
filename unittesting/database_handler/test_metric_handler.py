import unittest
from database.handler.metric_handler import create_from_frontend_json


class MyTestCase(unittest.TestCase):

    def test_1019(self):
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

    def test_1018(self):
        data = "abc"
        self.assertRaises(ValueError, create_from_frontend_json, data)


if __name__ == '__main__':
    unittest.main()
