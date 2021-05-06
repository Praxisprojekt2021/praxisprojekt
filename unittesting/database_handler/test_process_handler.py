import unittest
from database.handler.process_handler  import get_process, update_process, add_process, delete_process, add_process_reference, delete_process_reference, update_process_reference

class MyTestCase(unittest.TestCase):

    def test_2001(self):
        dict_in = {"uid": "1.5"}
        self.assertRaises(TypeError, get_process, dict_in)

    def test_1029(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(KeyError, get_process, dict_in)

    def test_21XX(self):
        dict_in = {"uid": "b141f94973a43cf8ee972e9dffc1b004"}
        result = {'success': True}
        self.assertEqual(update_process(dict_in), result)

    def test_2101(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc":{
                    "average":"a","min":"b","max":"c"}
            }
        }
        self.assertRaises(KeyError, add_process, dict_in)

    def test_1035X(self):
        dict_in = {"uid": "1"}
        result = "1"
        self.assertEqual(get_process(dict_in), result)

    def test_1035(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "gibtsnicht": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc":{
                    "average":"a","min":"b","max":"c"}
            }
        }
        self.assertRaises(KeyError, update_process, dict_in)

    def test_1026(self):
        dict_in = {"uid": "1"}
        result = {'success': True}
        self.assertEqual(get_process(dict_in), result)

    def test_2101(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "name": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc":{
                    "average":"a","min":"b","max":"c"}
            }
        }
        self.assertRaises(KeyError, add_process, dict_in)

    def test_1035X(self):
        dict_in = {"uid": "1"}
        result = "1"
        self.assertEqual(get_process(dict_in), result)

    def test_1035(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "gibtsnicht": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc":{
                    "average":"a","min":"b","max":"c"}
            }
        }
        self.assertRaises(KeyError, update_process, dict_in)

    def test_2203(self):
        dict_in = {"uid": "1.5"}
        self.assertRaises(TypeError, update_process, dict_in)

    def test_2203X(self):
        dict_in = {"uid": "1"}
        result = "1"
        self.assertEqual(update_process(dict_in), result)

    def test_1036(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(KeyError, update_process, dict_in)

    def test_1038(self):
        dict_in = {"uid": "abc"}
        self.assertRaises(KeyError, delete_process, dict_in)

    def test_1040(self):
        dict_in = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "gibtsnicht": "Kunde anlegen",
                "responsible_person": "Peter Rossbach",
                "description": "...."
            },
            "target_metrics": {
                "number_of_lines_of_source_code_loc":{
                    "average":"a","min":"b","max":"c"}
            }
        }
        self.assertRaises(KeyError, delete_process, dict_in)

    def test_1041(self):
        dict_in = {"uid": "1"}
        result = "1"
        self.assertEqual(add_process_reference(dict_in), result)

    def test_1043(self):
        dict_in = {
            "Test": "1",
            "Test": "2"
        }
        self.assertRaises(KeyError, add_process_reference, dict_in)

    def test_1044(self):
        dict_in = {
            "Test": "1",
            "Test": "2"
        }
        self.assertRaises(KeyError, delete_process_reference(), dict_in)

    def test_1045(self):
        dict_in = {"uid": "1", "weight": 2}
        result = {"1", 2}
        self.assertEqual(delete_process_reference(dict_in), result)

    def test_1046(self):
        dict_in = {
            "weight": "abc",
        }
        self.assertRaises(KeyError, delete_process_reference(), dict_in)

    def test_1080(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
        }
        result = {'success': True}
        self.assertEqual(delete_process(data), result)

    def test_1076(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",  # process uid not component uid
            "old_weight": 3,
            "new_weight": 2.5
        }
        result = {'success': True}
        self.assertEqual(update_process_reference(data), result)

    def test_1075(self):
        data = {
            "uid": "1.9",
            "old_weight": 3,
            "new_weight": 2.5
        }
        self.assertRaises(IndexError, update_process_reference, data)

    def test_1074(self):
        data = {
            "uid": "hahaha",
            "old_weight": 3,
            "new_weight": 2.5
        }
        self.assertRaises(IndexError, update_process_reference, data)

    def test_1073(self):
        data = {
            "uid": "999999999",
            "old_weight": 3,
            "new_weight": 2.5
        }
        self.assertRaises(IndexError, update_process_reference, data)

    def test_1070(self):
        data = {
            "process_uid": "hahaha",
            "component_uid": "b141f94973a43cf8ee972e9dffc1b005",
            "weight": 2.5
        }
        self.assertRaises(IndexError, add_process_reference, data)

    def test_1057(self):
        data = {
            "process": {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",  # when -1 it indicates that it is a new process, anything else indicates its an update
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


    def test_1055(self):
        data = {
            "process": {
                "uid": "hahaha",  # when -1 it indicates that it is a new process, anything else indicates its an update
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
        self.assertRaises(ValueError, update_process(), data)

    def test_1046(self):
        data = {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",  # process uid not component uid
            "weight": 2
        }
        result = {'success': True}
        self.assertEqual(delete_process_reference(data), result)

    def test_1079(self):
        data = {
            "uid": "1.9",
        }
        self.assertRaises(IndexError, delete_process_reference, data)

    def test_1078(self):
        data = {
            "uid": "hahaha",
        }
        self.assertRaises(IndexError, delete_process_reference, data)



if __name__ == '__main__':
    unittest.main()
