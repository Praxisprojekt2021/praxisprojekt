import unittest
from database.handler.component_handler import get_component, delete_component, update_component, add_component


class MyTestCase(unittest.TestCase):
    def test_1001(self):
        dict_in = {"uid": 1}
        result = 1
        self.assertEqual(get_component(dict_in), result)

    def test_1002(self):
        dict_in = {"uid": 1.5}
        self.assertRaises(TypeError, get_component, dict_in)

    def test_1003(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(IndexError, get_component, dict_in)

    def test_1004(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, get_component, dict_in)

    def test_1088(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000
            },
        }
        result = {'success': True}
        self.assertEqual(update_component(data), result)

    def test_1102(self):
        dict_in = {"uid": "1"}
        result = {'success': True}
        self.assertEqual(delete_component(dict_in), result)

    def test_1103(self):
        dict_in = {"uid": 1.5}
        self.assertRaises(TypeError, delete_component, dict_in)

    def test_1011(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, update_component, dict_in)

    def test_1012(self):
        dict_in = {"uid": "abc", "name": 2, "description": 3, "category": 4 , "metrics": 5}
        self.assertRaises(KeyError, update_component, dict_in)

    def test_10XX(self):
        dict_in = {"uid": "1"}
        result = {'success': True}
        self.assertEqual(delete_component(dict_in), result)

    def test_1015(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, add_component, dict_in)

    def test_1016(self):
        dict_in = {"uid": "abc", "name": 2, "description": 3, "category": 4 , "metrics": 5}
        self.assertRaises(KeyError, add_component, dict_in)

    def test_1014(self):
        data = {
            "uid": "-1",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        result = {'success': True}
        self.assertEqual(add_component(data), result)

    def test_1010(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        result = {'success': True}
        self.assertEqual(update_component(data), result)

    def test_1105(self):
        data = {
            "uid": "999666111",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        self.assertRaises(ValueError, delete_component, data)

    def test_1101(self):
        data = data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        result = {'success': True}
        self.assertEqual(delete_component(data), result)


    def test_1013(self):
        data = {
            "uid": "999666111",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        self.assertRaises(IndexError, update_component, data)

if __name__ == '__main__':
    unittest.main()
