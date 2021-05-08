import unittest
from database.handler.process_handler import get_process, update_process, add_process, delete_process, \
    add_process_reference, delete_process_reference, update_process_reference


class Test_get_process(unittest.TestCase):
    def test_2001(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
        }
        result = {'success': True}
        self.assertEqual(get_process(data), result)

    def test_2002(self):
        dict_in = {"uid": "1.5"}
        self.assertRaises(IndexError, get_process, dict_in)

    def test_2003(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(IndexError, get_process, dict_in)

    def test_2004(self):
        uid_dict = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, get_process, uid_dict)

    def test_2005(self):
        uid_dict = {"uid": "abc"}
        self.assertRaises(IndexError, get_process, uid_dict)


class Test_add_process(unittest.TestCase):

    def test_2101(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Kunden anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc": {
                    "average": "a", "min": "b", "max": "c"}
            }
        }
        self.assertRaises(ValueError, add_process, dict_in)

    def test_2102(self):
        input_dict = {
            "process": {
                "uid": "2.5",
                "name": "---",
                "description": "...."
            },
            "target_metrics": {"number_of_lines_of_source_code_loc":{"average":"a","min":"b","max":"c"}}
        }
        self.assertRaises(KeyError, add_process, input_dict)

    def test_2103(self):
        input_dict = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, add_process, input_dict)


class Test_update_process(unittest.TestCase):

    def test_2201(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "gibtsnicht": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc": {
                    "average": "a", "min": "b", "max": "c"}
            }
        }
        self.assertRaises(KeyError, update_process, dict_in)

    def test_2202(self):
        dict_in = {
            "process": {
                "uid": "2",
                "name": "Hallo",
                "description": "Hallo"
            },
            "target_metrics": {"number_of_lines_of_source_code_loc": {"average": 2, "min": 1, "max": 3}}
        }
        self.assertRaises(KeyError, update_process, dict_in)

    def test_2203(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Hallo",
                "description": "Hallo"
            },
            "target_metrics": {"number_of_lines_of_source_code_loc": {"average": 2, "min": 1, "max": 3}}
        }
        result = {'success': True}
        self.assertEqual(update_process(dict_in), result)

    def test_2204(self):
        dict_in = {
            "process": {
                "uid": "1.5",
                "name": "Hallo",
                "description": "Hallo"
            },
            "target_metrics": {"number_of_lines_of_source_code_loc": {"average": 2, "min": 1, "max": 3}}
        }
        self.assertRaises(KeyError, update_process, dict_in)

    def test_2205(self):
        uid_dict = {
            "process": {
                "uid": "22",
                "name": "Hallo",
                "description": "Hallo"
            },
            "target_metrics": {"number_of_lines_of_source_code_loc": {"average": 2, "min": 1, "max": 3}}
        }
        self.assertRaises(KeyError, update_process, uid_dict)

    def test_2206(self):
        data = {
            "process": {
                "uid": "hahaha",
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
        self.assertRaises(TypeError, update_process, data)

    def test_2207(self):
        data = {
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
        self.assertRaises(IndexError, update_process, data)

    def test_2208(self):
        data = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                # when -1 it indicates that it is a new process, anything else indicates its an update
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
        result = {'success': True}
        self.assertEqual(update_process(data), result)


class Test_delete_process(unittest.TestCase):
    def test_2301(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(KeyError, delete_process, dict_in)

    def test_2302(self):
        dict_in = {"test": 1, "test2": 2}
        self.assertRaises(KeyError, delete_process, dict_in)

    def test_2303(self):
        dict_in = {
            "process": {
                "uid": "2.5",
                "name": "---",
                "description": "...."
            },
            "target_metrics": {"number_of_lines_of_source_code_loc":{"average": "a", "min": "b", "max": "c"}}
        }
        self.assertRaises(KeyError, delete_process, dict_in)


class Test_add_process_reference(unittest.TestCase):
    def test_2401(self):
        dict_in = {
            "process_uid": "b141f94973a43cf8ee972e9dffc1b004",
            "component_uid": "b141f94973a43cf8ee972e9dffc1b005",
            "weight": 2.5
        }
        result = {'success': True}
        self.assertEqual(add_process_reference(dict_in), result)

    def test_2402(self):
        dict_in = {
            "Test": "1",
            "Test": "2"
        }
        self.assertRaises(KeyError, add_process_reference, dict_in)

    def test_2403(self):
        data = {
            "process_uid": "hahaha",
            "component_uid": "b141f94973a43cf8ee972e9dffc1b005",
            "weight": 2.5
        }
        self.assertRaises(TypeError, add_process_reference, data)


class Test_delete_process_reference(unittest.TestCase):
    def test_2501(self):
        dict_in = {
            "Test": "1",
            "Test": "2"
        }
        self.assertRaises(KeyError, delete_process_reference, dict_in)

    def test_2502(self):
        dict_in = {"uid": "b141f94973a43cf8ee972e9dffc1b004", "weight": 2}
        result = {'success': True}
        self.assertEqual(delete_process_reference(dict_in), result)

    def test_2504(self):
        data = {
            "uid": "hahaha",
            "weight": 2
        }
        self.assertRaises(IndexError, delete_process_reference, data)

    def test_2505(self):
        data = {
            "uid": "1.9",
            "weight": 2
        }
        self.assertRaises(IndexError, delete_process_reference, data)


class Test_update_process_reference(unittest.TestCase):
    def test_2601(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",  # process uid not component uid
            "old_weight": 3,
            "new_weight": 2.5
        }
        result = {'success': True}
        self.assertEqual(update_process_reference(data), result)

    def test_2602(self):
        data = {
            "uid": "hahaha",
            "old_weight": 3,
            "new_weight": 2.5
        }
        self.assertRaises(IndexError, update_process_reference, data)

    def test_2603(self):
        data = {
            "uid": "1.9",
            "old_weight": 3,
            "new_weight": 2.5
        }
        self.assertRaises(IndexError, update_process_reference, data)


if __name__ == '__main__':
    unittest.main()
