import unittest
from database.handler.component_handler import get_component, delete_component

class MyTestCase(unittest.TestCase):
    def test_1002(self):
        dict_in = {"uid": 1.5}
        self.assertRaises(TypeError, get_component, dict_in)

    def test_1003(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(IndexError, get_component, dict_in)


if __name__ == '__main__':
    unittest.main()
