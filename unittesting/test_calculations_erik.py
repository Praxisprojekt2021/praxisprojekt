import unittest
import processing.calculations as calc
import database.handler.metric_handler as metric_handler


process_dict = {
    "success": True,
    "process": {
        "uid": "b141f94973a43cf8ee972e9dffc1b004",
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
        "components": [
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1,  # different from single component view!
                "name": "SQL Datenbank",
                "category": "Datenbank",
                "description": "Kundendatenbank",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1.5,
                "name": "Frontend API",
                "category": "API",
                "description": "API für das Frontend",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 2,
                "name": "Hadoop Cluster",
                "category": "Datenbank",
                "description": "Big Data Plattform",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            }
            # ...
        ]
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
        # ...
    },
}

process_dict1 = {
    "success": True,
    "process": {
        "uid": "b141f94973a43cf8ee972e9dffc1b004",
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
        "components": [
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1,  # different from single component view!
                "name": "SQL Datenbank",
                "category": "Datenbank",
                "description": "Kundendatenbank",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "admins": 10,
                    "codelines": 20000,
                    "recovery_time": 5,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1.5,
                "name": "Frontend API",
                "category": "API",
                "description": "API für das Frontend",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 2,
                "name": "Hadoop Cluster",
                "category": "Datenbank",
                "description": "Big Data Plattform",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            }
            # ...
        ]
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
        # ...
    },
}
process_dict2 = {
    "success": True,
    "process": {
        "uid": "b141f94973a43cf8ee972e9dffc1b004",
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
        "components": [
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1,  # different from single component view!
                "name": "SQL Datenbank",
                "category": "Datenbank",
                "description": "Kundendatenbank",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "recovery_time": 5,
                    "admins": 10,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1.5,
                "name": "Frontend API",
                "category": "API",
                "description": "API für das Frontend",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 2,
                "name": "Hadoop Cluster",
                "category": "Datenbank",
                "description": "Big Data Plattform",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            }
            # ...
        ]
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
        # ...
    },
}
process_dict3 = {
    "success": True,
    "process": {
        "uid": "b141f94973a43cf8ee972e9dffc1b004",
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
        "components": [
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1,  # different from single component view!
                "name": "SQL Datenbank",
                "category": "Datenbank",
                "description": "Kundendatenbank",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "admins": 10,
                    "recovery_time": 5,
                    "codelines": 20000,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 1.5,
                "name": "Frontend API",
                "category": "API",
                "description": "API für das Frontend",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            },
            {
                "uid": "b141f94973a43cf8ee972e9dffc1b004",
                "weight": 2,
                "name": "Hadoop Cluster",
                "category": "Datenbank",
                "description": "Big Data Plattform",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": {
                    "codelines": 20000,
                    "admins": 10,
                    "recovery_time": 5,
                    # ...
                }
            }
            # ...
        ]
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
        # ...
    },
}


#metrics_dict = metric_handler.get_metrics_data()
#print(metrics_dict)

#4200
component_metrics = calc.get_all_component_metrics(process_dict)
#print(component_metrics)
test1_component_metrics = {'codelines': [20000, 20000, 20000], 'admins': [10, 10, 10], 'recovery_time': [5, 5, 5]}

#4300
#target_metrics = calc.get_all_target_metrics(process_dict)
#print(target_metrics)


class TestCalc(unittest.TestCase):

    def test_compare_actual_target_metrics(self):
        self.assertEqual(calc.get_all_component_metrics(process_dict1),
                         test1_component_metrics),
        self.assertEqual(calc.get_all_component_metrics(process_dict2),
                         test1_component_metrics),
        self.assertEqual(calc.get_all_component_metrics(process_dict3),
                         test1_component_metrics),
#print(process_dict)
#print(component_metrics)
#print(test1_component_metrics)


if __name__ == '__main__':
    unittest.main()

