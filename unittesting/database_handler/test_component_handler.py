import unittest
from database.handler.component_handler import get_component, delete_component, update_component, add_component


class Test_get_component(unittest.TestCase):
    def test_1001(self):
        dict_in = {
            "process": {
                "uid": "4c4daea7bd0c46ba9aa0b73bda06e58f",  # when -1 it indicates that it is a new process, anything else indicates its an update
                "name": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            },
            "target_metrics": {
                "codelines": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                },
                "admins": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                },

            },
        }
        result_1001 = {
            'success': True,
            'component':
                {'uid': '4c4daea7bd0c46ba9aa0b73bda06e58f',
                 'last_timestamp': '2021-05-05 20:06:48.137547',
                 'creation_timestamp': '2021-05-02 13:56:26.715471',
                 'name': 'Enterprise_Comp',
                 'description': 'Important Test',
                 'category': 'standardized_software',
                 'metrics':
                     {'encryption': 1,
                      'number_of_administrators': 9,
                      'redundancy': 1,
                      'planned_maintenance_percentage': 7,
                      'restore_time': 7,
                      'time_between_failures': 7,
                      'maximum_downtime_at_a_time': 5,
                      'downtime': 5, 'restart': 3,
                      'number_of_views_per_day': 3,
                      'internal_support': 1,
                      'external_support': 0,
                      'time_to_implement_updates': 6,
                      'automation': 0,
                      'training': 1,
                      'complaints': 5,
                      'patch_status_check': 12,
                      'change_tracking': 0,
                      'back-up': 9}}}
        self.assertEqual(get_component(dict_in), result_1001)

    def test_1002(self):
        dict_in = {
            "process": {
                "uid": "1.5",  # when -1 it indicates that it is a new process, anything else indicates its an update
                "name": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            },
            "target_metrics": {
                "codelines": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                },
                "admins": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                },

            },
        }
        self.assertRaises(KeyError, get_component, dict_in)

    def test_1003(self):
        dict_in = {
            "process": {
                "uid": "abc",  # when -1 it indicates that it is a new process, anything else indicates its an update
                "name": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            },
            "target_metrics": {
                "codelines": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                },
                "admins": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                },

            },
        }
        self.assertRaises(KeyError, get_component, dict_in)

    def test_1004(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, get_component, dict_in)


class Test_delete_component(unittest.TestCase):
    def test_1101(self):
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
        self.assertEqual(delete_component(data), result)


    def test_1102(self):
        dict_in = {
            "uid": "1.5",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        self.assertRaises(TypeError, delete_component, dict_in)

    def test_1103(self):
        data = {
            "uid": "abc",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5,
            },
        }
        self.assertRaises(KeyError, delete_component, data)

    def test_1104(self):
        data = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, delete_component, data)

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


class Test_update_component(unittest.TestCase):
    def test_1201(self):
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

    def test_1202(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, update_component, dict_in)

    def test_1203(self):
        dict_in = {
            "uid": "abc",
            "name": 2,
            "category": 3,
            "description": 4,
            "metrics": {
                "codelines": "zwei",
                "admins": "drei",
                "recovery_time": "fuenf",
            },
        }
        self.assertRaises(ValueError, update_component, dict_in)

    def test_1204(self):
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

    def test_1205(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "SQL Datenbank",
            "category": "Datenbank",
            "description": "Datenbank zu xy mit ...",
            "metrics": {
                "codelines": 20000,
                "admins": 10,
                "recovery_time": 5
            },
        }
        result = {'success': True}
        self.assertEqual(update_component(data), result)


class Test_add_component(unittest.TestCase):

    def test_1301(self):
        dict_in = {
            "uid": "b141f94973a43cf8ee972e9dffc1b009",
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
        self.assertEqual(delete_component(dict_in), result)

    def test_1302(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, add_component, dict_in)

    def test_1304(self):
        dict_in = {
            "uid": "abc",
            "name": 2,
            "category": 3,
            "description": 4,
            "metrics": {
                "codelines": "zwei",
                "admins": "zehn",
                "recovery_time": "fuenf",
            }
        }
        self.assertRaises(KeyError, add_component, dict_in)


if __name__ == '__main__':
    unittest.main()
