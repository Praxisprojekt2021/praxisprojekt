import unittest
import processing.calculations as calc
import database.handler.metric_handler as metric_handler

##multiple used dicts (for various functions)
"""
metrics_dict = metric_handler.get_metrics_data()
print(metrics_dict)
component_metrics = calc.get_all_component_metrics(process_dict)
print(component_metrics)
print(process_dict)
print(component_metrics)
print(test1_component_metrics)
"""

#42xx - get_all_component_metrics

#process_dicts with different component metric values
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

#process dicts with order changes of component metrics, but identically values from test1_4201_process_dict -> test1_4201_component_metrics
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

#test1_4201_component_metrics = calc.get_all_component_metrics(test1_4201_process_dict)
#test2_4201_component_metrics = calc.get_all_component_metrics(test2_4201_process_dict)
#test3_4201_component_metrics = calc.get_all_component_metrics(test3_4201_process_dict)


class TestCalc(unittest.TestCase):

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



#43xx - get_all_target_metrics

#process_dicts with different target metric values
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

#process dicts with order changes of target metrics, but identically values from test1_4301_process_dict -> test1_4301_component_metrics
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

test1_4301_target_metrics = calc.get_all_target_metrics(test1_4301_process_dict)
test2_4301_target_metrics = calc.get_all_target_metrics(test2_4301_process_dict)
test3_4301_target_metrics = calc.get_all_target_metrics(test3_4301_process_dict)


class TestCalc2(unittest.TestCase):

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
        self.assertEqual(calc.get_all_target_metrics(test1_4202_process_dict),
                         test1_4301_target_metrics),
        self.assertEqual(calc.get_all_target_metrics(test2_4202_process_dict),
                         test1_4301_target_metrics),
        self.assertEqual(calc.get_all_target_metrics(test3_4202_process_dict),
                         test1_4301_target_metrics)


#44xx - calculate_current_values (metrics_dict: dict, component_metrics, target_metrics)
no_target_process_dict={ 
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
       
    },
}
no_target_no_metric_process_dict={
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
component_metrics=calc.get_all_component_metrics(no_target_process_dict)
target_metrics=calc.get_all_target_metrics(no_target_process_dict) 
test_calculate_current_values_1= calc.calculate_current_values(metrics_dict, component_metrics, target_metrics )
{'number_of_lines_of_source_code_loc': {'actual': {'total': 60000, 'min': 20000, 'max': 20000, 'average': 20000, 'standard_deviation': 0.0}, 'count_component': 3, 'target': {'average': 50, 'min': 30.5, 'max': 20, 'total': 150}}, 'time_to_implement_updates': {'actual': {'total': 15, 'min': 5, 'max': 5, 'average': 5, 'standard_deviation': 0.0}, 'count_component': 3}}
class TestCalc3 (unittest.TestCase):

    def test_calculate_current_values_4401(self): 
        print('4401-Wenn kein Target-Wert vorhanden ist, keine Anlegen von Targetkey ')
        self.assertRaises(KeyError, test_calculate_current_values_1['time_to_implement_updates'].__getitem__, 'target')
    def test_calculate_current_values_4402(self):
        print('4402-Target wird richtig berechnet')
        self.assertEqual(test_calculate_current_values_1['number_of_lines_of_source_code_loc'] ['target']['total'],
                        150 )
    def test_calculate_current_values_4403(self):
        component_metrics=calc.get_all_component_metrics(no_target_no_metric_process_dict)
        target_metrics=calc.get_all_target_metrics(no_target_no_metric_process_dict)
        test_calculate_current_values_2= calc.calculate_current_values(metrics_dict, component_metrics, target_metrics )
        print('4403- Rückgabe leerer Metric, falls proccess_target_flage und component metric flag false sind')
        self.assertEqual(test_calculate_current_values_2, {})

#print(component_metrics)
#print(metrics_dict)S
#print(target_metrics)
class TestClac4 (unittest.TestCase):
    var1=[20000, 20000, 20000]
    var2=[5, 5, 5]
    def test_calculate_actual_values_4501(self):
        print('4501- Richtige Berechnung des Totals')
        var1=[20000, 20000, 20000]
        self.assertEqual(calc.calculate_actual_values(var1)['actual']['total'],60000 )
    def test_calculate_actual_values_4502(self):
        print('4502- Richtige Berechung des Min')
        var1=[30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(var1)['actual']['min'],10000)
    def test_calculate_actual_values_4503(self):
        print('4503- Richtige Berechung des Max')
        var1=[30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(var1)['actual']['max'],40000)
    def test_calculate_actual_values_4504(self):
        print('4504- Richtige Berechung des Standard_deviation')
        var1=[30000, 10000, 40000]
        self.assertEqual(calc.calculate_actual_values(var1)['actual']['standard_deviation'],15275.252316519465)

if __name__ == '__main__':
    unittest.main()
