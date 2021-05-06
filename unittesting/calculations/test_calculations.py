import unittest
import processing.calculations as calc
import database.handler.metric_handler as metric_handler
import json

# 42xx - get_all_component_metrics

# process_dicts with different component metric values
test1_4201_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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
test2_4201_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 40000,
                    "admins": 20,
                    "time_to_implement_updates": 10,
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
                    "number_of_lines_of_source_code_loc": 10000,
                    "admins": 5,
                    "time_to_implement_updates": 3,
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
                    "number_of_lines_of_source_code_loc": 50000,
                    "admins": 70,
                    "time_to_implement_updates": 50,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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
test3_4201_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 50000,
                    "admins": 70,
                    "time_to_implement_updates": 4,
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
                    "number_of_lines_of_source_code_loc": 40000,
                    "admins": 50,
                    "time_to_implement_updates": 6,
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
                    "number_of_lines_of_source_code_loc": 50000,
                    "admins": 60,
                    "time_to_implement_updates": 4,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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

# process dicts with order changes of component metrics, but identically values from test1_4201_process_dict -> test1_4201_component_metrics
test1_4202_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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
test2_4202_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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
test3_4202_process_dict = {
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
                    "time_to_implement_updates": 5,
                    "number_of_lines_of_source_code_loc": 20000,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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

# test1_4201_component_metrics = calc.get_all_component_metrics(test1_4201_process_dict)
# print(test1_4201_component_metrics)
test1_4201_component_metrics = {'number_of_lines_of_source_code_loc': [20000, 20000, 20000], 'admins': [10, 10, 10],
                                'time_to_implement_updates': [5, 5, 5]}
# test2_4201_component_metrics = calc.get_all_component_metrics(test2_4201_process_dict)
# print(test2_4201_component_metrics)
test2_4201_component_metrics = {'number_of_lines_of_source_code_loc': [40000, 10000, 50000], 'admins': [20, 5, 70],
                                'time_to_implement_updates': [10, 3, 50]}
# test3_4201_component_metrics = calc.get_all_component_metrics(test3_4201_process_dict)
# print(test3_4201_component_metrics)
test3_4201_component_metrics = {'number_of_lines_of_source_code_loc': [50000, 40000, 50000], 'admins': [70, 50, 60],
                                'time_to_implement_updates': [4, 6, 4]}


class Test_get_all_component_metrics(unittest.TestCase):

    def test_get_all_component_metrics_4201(self):
        print('4201 - Überprüfen, ob alle Metriken ausgelesen werden')
        self.assertEqual(calc.get_all_component_metrics(test1_4201_process_dict),
                         test1_4201_component_metrics),
        self.assertEqual(calc.get_all_component_metrics(test2_4201_process_dict),
                         test2_4201_component_metrics),
        self.assertEqual(calc.get_all_component_metrics(test3_4201_process_dict),
                         test3_4201_component_metrics)

    def test_get_all_component_metrics_4202(self):
        print('4202 - Überprüfen, ob die Reihenfolge der process_dict Elemente variieren kann')
        self.assertEqual(calc.get_all_component_metrics(test1_4202_process_dict),
                         test1_4201_component_metrics),
        self.assertEqual(calc.get_all_component_metrics(test2_4202_process_dict),
                         test1_4201_component_metrics),
        self.assertEqual(calc.get_all_component_metrics(test3_4202_process_dict),
                         test1_4201_component_metrics)


# 43xx - get_all_target_metrics

# process_dicts with different target metric values
test1_4301_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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
test2_4301_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "average": 500,
            "min": 300.5,
            "max": 200,
        },
        "admins": {
            "average": 500,
            "min": 300.5,
            "max": 200,
        },
        # ...
    },
}
test3_4301_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "average": 5000,
            "min": 3000.5,
            "max": 2000,
        },
        "admins": {
            "average": 5000,
            "min": 3000.5,
            "max": 2000,
        },
        # ...
    },
}

# process dicts with order changes of target metrics, but identically values from test1_4301_process_dict ->
# test1_4301_target_metrics
test1_4302_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "min": 30.5,
            "average": 50,
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
test2_4302_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "average": 50,
            "max": 20,
            "min": 30.5,
        },
        "admins": {
            "average": 50,
            "min": 30.5,
            "max": 20,
        },
        # ...
    },
}
test3_4302_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "min": 30.5,
            "max": 20,
            "average": 50,
        },
        "admins": {
            "average": 50,
            "min": 30.5,
            "max": 20,
        },
        # ...
    },
}

# test1_4301_target_metrics = calc.get_all_target_metrics(test1_4301_process_dict)
# print(test1_4301_target_metrics)
test1_4301_target_metrics = {'number_of_lines_of_source_code_loc': {'target': {'average': 50, 'min': 30.5, 'max': 20}},
                             'admins': {'target': {'average': 50, 'min': 30.5, 'max': 20}}}
# test2_4301_target_metrics = calc.get_all_target_metrics(test2_4301_process_dict)
# print(test2_4301_target_metrics)
test2_4301_target_metrics = {
    'number_of_lines_of_source_code_loc': {'target': {'average': 500, 'min': 300.5, 'max': 200}},
    'admins': {'target': {'average': 500, 'min': 300.5, 'max': 200}}}
# test3_4301_target_metrics = calc.get_all_target_metrics(test3_4301_process_dict)
# print(test3_4301_target_metrics)
test3_4301_target_metrics = {
    'number_of_lines_of_source_code_loc': {'target': {'average': 5000, 'min': 3000.5, 'max': 2000}},
    'admins': {'target': {'average': 5000, 'min': 3000.5, 'max': 2000}}}


class Test_get_all_target_metrics(unittest.TestCase):

    def test_get_all_target_metrics_4201(self):
        print('4301 - Überprüfen, ob alle Metriken ausgelesen werden')
        self.assertEqual(calc.get_all_target_metrics(test1_4301_process_dict),
                         test1_4301_target_metrics),
        self.assertEqual(calc.get_all_target_metrics(test2_4301_process_dict),
                         test2_4301_target_metrics),
        self.assertEqual(calc.get_all_target_metrics(test3_4301_process_dict),
                         test3_4301_target_metrics)

    def test_get_all_target_metrics_4202(self):
        print('4302 - Überprüfen, ob die Reihenfolge der process_dict Elemente variieren kann')
        self.assertEqual(calc.get_all_target_metrics(test1_4302_process_dict),
                         test1_4301_target_metrics)
        self.assertEqual(calc.get_all_target_metrics(test2_4302_process_dict),
                         test1_4301_target_metrics),
        self.assertEqual(calc.get_all_target_metrics(test3_4302_process_dict),
                         test1_4301_target_metrics)


# 44xx - calculate_current_values (metrics_dict: dict, component_metrics, target_metrics)
no_target_process_dict = data = {
    "success": True,
    "process": {
        "uid": "b141f94973a43cf8ee972e9dffc1b004",
        "name": "Kunde anlegen",
        "responsible_person": "Peter Rossbach",
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 20000,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    # nach risk calc dann nicht mehr drin
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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
    # ab jetzt erst ab Backend durch Risk calc
    "score": 80,  # percent as integer
    "actual_target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "actual": {
                "average": 30,
                "max": 50,
                "min": 20,
                "standard_deviation": 5,
                "total": 300,  # summe
            },
            "target": {
                "average": 30,
                "total": 300,  # summe
            },
            "count_component": 10,
            "fulfillment": True
        },  # true means that the metric is fulfilled --> no problem.
        "admins": {
            "actual": {
                "average": 30,
                "max": 50,
                "min": 20,
                "standard_deviation": 5,
                "total": 300,  # summe
            },
            "target": {
                "average": 30,
                "total": 300,  # summe
            },
            "count_component": 10,
            "fulfillment": True
        },
        "time_to_implement_updates": {
            "actual": {
                "average": 0.65,
                "max": 0.8,
                "min": 0.5,
                "standard_deviation": 5,
                "total": 0.4,  # summe
            },
            "target": {
                "average": 0.8,
                "total": 0.64,  # summe
            },
            "count_component": 2,
            "fulfillment": True
        },  # false means that the metric is not fulfilled --> problem.
    }
}
no_target_no_metric_process_dict = {
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

                }
            }
            # ...
        ]
    },
    "target_metrics": {

    },
}

metrics_dict = metric_handler.get_metrics_data()
component_metrics = calc.get_all_component_metrics(no_target_process_dict)
target_metrics = calc.get_all_target_metrics(no_target_process_dict)
test_calculate_current_values_1 = calc.calculate_current_values(metrics_dict, component_metrics, target_metrics)


class Test_calculate_current_values(unittest.TestCase):

    def test_calculate_current_values_4401(self):
        print('4401 - Wenn kein Target-Wert vorhanden ist, keine Anlegen von Targetkey ')
        self.assertRaises(KeyError, test_calculate_current_values_1['time_to_implement_updates'].__getitem__, 'target')

    def test_calculate_current_values_4402(self):
        print('4402 - Target wird richtig berechnet')
        self.assertEqual(test_calculate_current_values_1['number_of_lines_of_source_code_loc']['target']['total'],
                         150)

    def test_calculate_current_values_4403(self):
        component_metrics = calc.get_all_component_metrics(no_target_no_metric_process_dict)
        target_metrics = calc.get_all_target_metrics(no_target_no_metric_process_dict)
        test_calculate_current_values_2 = calc.calculate_current_values(metrics_dict, component_metrics, target_metrics)
        print('4403 - Rückgabe leerer Metric, falls proccess_target_flage und component metric flag false sind')
        self.assertEqual(test_calculate_current_values_2, {})


# 45xx - calculate_actual_values (metrics_dict: dict, component_metrics, target_metrics)

class Test_calculate_actual_values(unittest.TestCase):
    def test_calculate_actual_values_4501(self):
        print('4501 - Richtige Berechnung des Totals')
        actual_component_metric_data = [20000, 20000, 20000]
        self.assertEqual(calc.calculate_actual_values(actual_component_metric_data)['actual']['total'], 60000)

    def test_calculate_actual_values_4502(self):
        print('4502 - Richtige Berechung des Min')
        actual_component_metric_data = [30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(actual_component_metric_data)['actual']['min'], 10000)

    def test_calculate_actual_values_4503(self):
        print('4503 - Richtige Berechung des Max')
        actual_component_metric_data = [30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(actual_component_metric_data)['actual']['max'], 40000)

    def test_calculate_actual_values_4504(self):
        print('4504 - Richtige Berechung des Standard_deviation')
        actual_component_metric_data = [30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(actual_component_metric_data)['actual']['standard_deviation'],
                         15275.252316519465)

    def test_calculate_actual_values_4505(self):
        print('4505 - Richtige Berechnung des Average')
        actual_component_metric_data = [30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(actual_component_metric_data)['actual']['average'],
                         26666.666666666668)

    def test_calculate_actual_values_4506(self):
        print('4506 - Überprüfen, ob die Anzahl der Komponenten richtig berechnet wird')
        actual_component_metric_data = [30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(actual_component_metric_data)['count_component'], 3)


# 46xx - compare_actual_target_metrics(process_dict, metrics_dict)

# output_dict = output from calculate_current_values()
output_dict = {'success': no_target_process_dict["success"], 'process': no_target_process_dict["process"],
               'actual_target_metrics': {}}
output_dict['actual_target_metrics'] = test_calculate_current_values_1
outcome_compare_actual_target_metrics = {'success': True,
                                         'process': {'uid': 'b141f94973a43cf8ee972e9dffc1b004', 'name': 'Kunde anlegen',
                                                     'responsible_person': 'Peter Rossbach',
                                                     'description': 'Prozess zum anlegen von einem neuen Kunden in allen Systemen',
                                                     'creation_timestamp': '20210210...',
                                                     'last_timestamp': '20200211...', 'components': [
                                                 {'uid': 'b141f94973a43cf8ee972e9dffc1b004', 'weight': 1,
                                                  'name': 'SQL Datenbank', 'category': 'Datenbank',
                                                  'description': 'Kundendatenbank', 'creation_timestamp': '20200219...',
                                                  'last_timestamp': '20200219...',
                                                  'metrics': {'number_of_lines_of_source_code_loc': 20000, 'admins': 10,
                                                              'time_to_implement_updates': 5}},
                                                 {'uid': 'b141f94973a43cf8ee972e9dffc1b004', 'weight': 1.5,
                                                  'name': 'Frontend API', 'category': 'API',
                                                  'description': 'API für das Frontend',
                                                  'creation_timestamp': '20200219...', 'last_timestamp': '20200219...',
                                                  'metrics': {'number_of_lines_of_source_code_loc': 20000, 'admins': 10,
                                                              'time_to_implement_updates': 5}},
                                                 {'uid': 'b141f94973a43cf8ee972e9dffc1b004', 'weight': 2,
                                                  'name': 'Hadoop Cluster', 'category': 'Datenbank',
                                                  'description': 'Big Data Plattform',
                                                  'creation_timestamp': '20200219...', 'last_timestamp': '20200219...',
                                                  'metrics': {'number_of_lines_of_source_code_loc': 20000, 'admins': 10,
                                                              'time_to_implement_updates': 5}}]},
                                         'actual_target_metrics': {'number_of_lines_of_source_code_loc': {
                                             'actual': {'total': 60000, 'min': 20000, 'max': 20000, 'average': 20000,
                                                        'standard_deviation': 0.0}, 'count_component': 3,
                                             'target': {'average': 50, 'min': 30.5, 'max': 20, 'total': 150},
                                             'fulfillment': False}, 'time_to_implement_updates': {
                                             'actual': {'total': 15, 'min': 5, 'max': 5, 'average': 5,
                                                        'standard_deviation': 0.0}, 'count_component': 3}}}
outcome_compare_actual_target_metrics_dict = \
    {
        "success": True,
        "process": {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde anlegen",
            "responsible_person": "Peter Rossbach",
            "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            "components": [
                {
                    "uid": "b141f94973a43cf8ee972e9dffc1b004",
                    "weight": 1,
                    "name": "SQL Datenbank",
                    "category": "Datenbank",
                    "description": "Kundendatenbank",
                    "creation_timestamp": "20200219...",
                    "last_timestamp": "20200219...",
                    "metrics": {
                        "number_of_lines_of_source_code_loc": 20000,
                        "admins": 10,
                        "time_to_implement_updates": 5
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
                        "number_of_lines_of_source_code_loc": 20000,
                        "admins": 10,
                        "time_to_implement_updates": 5
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
                        "number_of_lines_of_source_code_loc": 20000,
                        "admins": 10,
                        "time_to_implement_updates": 5
                    }
                }
            ]
        },
        "actual_target_metrics": {
            "number_of_lines_of_source_code_loc": {
                "actual": {
                    "total": 60000,
                    "min": 20000,
                    "max": 20000,
                    "average": 20000,
                    "standard_deviation": 0.0
                },
                "count_component": 3,
                "target": {
                    "average": 50,
                    "min": 30.5,
                    "max": 20,
                    "total": 150
                },
                "fulfillment": False
            },
            "time_to_implement_updates": {
                "actual": {
                    "total": 15,
                    "min": 5,
                    "max": 5,
                    "average": 5,
                    "standard_deviation": 0.0
                },
                "count_component": 3
            }
        }
    }

# dict -> String, da Fehlermeldung bei dict
var_outcome_compare_actual_target_metrics = json.dumps(outcome_compare_actual_target_metrics)


class Test_compare_actual_target_metrics(unittest.TestCase):

    def test_compare_actual_target_metrics_4601(self):
        print('4601 - Überprüfen, ob alle Metriken korrekt ausgelesen werden')
        self.assertIn(json.dumps(calc.compare_actual_target_metrics(output_dict, metrics_dict)),
                      var_outcome_compare_actual_target_metrics)

#TODO: Aaron, bitte Kommentar hier lassen
"""
    def test_compare_actual_target_metrics_4602(self):
        print('4602 - Überprüfen, ob fulfilled erkannt wird, wenn MIN(actual=target)')
        #...

    def test_compare_actual_target_metrics_4603(self):
        print('4603 - Überprüfen, ob fulfilled erkannt wird, wenn MAX(actual=target)')
        #...

    def test_compare_actual_target_metrics_4604(self):
        print('4604 - Überprüfen, ob fulfilled erkannt wird, wenn AVERAGE(actual=target)')
        #...
"""

# 47xx - calculate_risk_score(process_dict: dict) -> dict:

# process_dict = outcome_compare_actual_target_metrics = output from compare_actual_target_metrics()
outcome_calculate_risk_score = calc.calculate_risk_score(outcome_compare_actual_target_metrics)


class Test_calculate_risk_score(unittest.TestCase):

    def test_compare_actual_target_metrics_4701(self):
        print(
            '4701 - Überprüfen, ob der Score richtig berechnet wurde, insofern mindestens eine metrik den Anforderungen entsprach')
        self.assertEqual(calc.calculate_risk_score(outcome_compare_actual_target_metrics),
                         outcome_calculate_risk_score)


"""
    def test_compare_actual_target_metrics_4702(self):
        print('4702 - Überprüfen, ob der Score 0 beträgt, insofern keine metrik den Anforderungen entsprach')
        self.assertEqual(calc.calculate_risk_score(outcome_compare_actual_target_metrics),
                         outcome_calculate_risk_score)

    def test_compare_actual_target_metrics_4703(self):
        print('4703 - Überprüfen, ob ein Score über 100% erreicht werden kann. (actual value > target value sollte nicht möglich sein)')
        self.assertEqual(calc.calculate_risk_score(outcome_compare_actual_target_metrics),
                         outcome_calculate_risk_score)
"""

# 41xx - start_calculate_risk(process_dict: dict, metrics_dict: dict) -> dict:
"""
test1_4101_process_dict = {
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
                    "number_of_lines_of_source_code_loc": 10,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 10,
                    "admins": 10,
                    "time_to_implement_updates": 5,
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
                    "number_of_lines_of_source_code_loc": 10,
                    "admins": 10,
                    "time_to_implement_updates": 5,
                    # ...
                }
            }
            # ...
        ]
    },
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
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

#outcome_start_calculate_risk = calc.start_calculate_risk(test1_4101_process_dict, metrics_dict)
outcome_start_calculate_risk = \
    {
        "success":True,
        "process":{
            "uid":"b141f94973a43cf8ee972e9dffc1b004",
            "name":"Kunde anlegen",
            "responsible_person":"Peter Rossbach",
            "description":"Prozess zum anlegen von einem neuen Kunden in allen Systemen",
            "creation_timestamp":"20210210...",
            "last_timestamp":"20200211...",
            "components":[
                {
                    "uid":"b141f94973a43cf8ee972e9dffc1b004",
                    "weight":1,
                    "name":"SQL Datenbank",
                    "category":"Datenbank",
                    "description":"Kundendatenbank",
                    "creation_timestamp":"20200219...",
                    "last_timestamp":"20200219...",
                    "metrics":{
                        "number_of_lines_of_source_code_loc":20000,
                        "admins":10,
                        "time_to_implement_updates":5
                    }
                },
                {
                    "uid":"b141f94973a43cf8ee972e9dffc1b004",
                    "weight":1.5,
                    "name":"Frontend API",
                    "category":"API",
                    "description":"API für das Frontend",
                    "creation_timestamp":"20200219...",
                    "last_timestamp":"20200219...",
                    "metrics":{
                        "number_of_lines_of_source_code_loc":20000,
                        "admins":10,
                        "time_to_implement_updates":5
                    }
                },
                {
                    "uid":"b141f94973a43cf8ee972e9dffc1b004",
                    "weight":2,
                    "name":"Hadoop Cluster",
                    "category":"Datenbank",
                    "description":"Big Data Plattform",
                    "creation_timestamp":"20200219...",
                    "last_timestamp":"20200219...",
                    "metrics":{
                        "number_of_lines_of_source_code_loc":20000,
                        "admins":10,
                        "time_to_implement_updates":5
                    }
                }
            ]
        },
        "actual_target_metrics":{
            "number_of_lines_of_source_code_loc":{
                "actual":{
                    "total":60000,
                    "min":20000,
                    "max":20000,
                    "average":20000,
                    "standard_deviation":0.0
                },
                "count_component":3,
                "target":{
                    "average":50,
                    "min":30.5,
                    "max":20,
                    "total":150
                },
                "fulfillment":False
            },
            "time_to_implement_updates":{
                "actual":{
                    "total":15,
                    "min":5,
                    "max":5,
                    "average":5,
                    "standard_deviation":0.0
                },
                "count_component":3
            }
        }
    }

class Test_start_calculate_risk(unittest.TestCase):

    def test_compare_actual_target_metrics_4701(self):
        print('4101 - Überprüfen, ob alle Funktionen erfolgreich durchlaufen wurden')
        self.assertEqual(calc.start_calculate_risk(test1_4101_process_dict, metrics_dict),
                         outcome_start_calculate_risk)

"""

if __name__ == '__main__':
    unittest.main()
