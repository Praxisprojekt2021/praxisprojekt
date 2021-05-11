PROCESS_DICT_HEAD = {
    "success": True,
    "process": {
        "uid": "b141f94973a43cf8ee972e9dffc1b004",
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211..."
    }
}

COMPONENT_ALL_METRICS_1 = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
    "weight": 1,  # different from single component view!
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Kundendatenbank",
    "creation_timestamp": "20200219...",
    "last_timestamp": "20200219...",
    "metrics": {
        "number_of_lines_of_source_code_loc": 20000,
        "number_of_administrators": 10,
        "time_to_implement_updates": 5
    }
}

COMPONENT_ALL_METRICS_2 = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
    "weight": 1,  # different from single component view!
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Kundendatenbank",
    "creation_timestamp": "20200219...",
    "last_timestamp": "20200219...",
    "metrics": {
        "number_of_lines_of_source_code_loc": 12000,
        "number_of_administrators": 12,
        "time_to_implement_updates": 3
    }
}

COMPONENT_FEW_METRICS = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
    "weight": 1,  # different from single component view!
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Kundendatenbank",
    "creation_timestamp": "20200219...",
    "last_timestamp": "20200219...",
    "metrics": {
        "number_of_lines_of_source_code_loc": 5000
    }
}

PROCESS_ALL_TARGET_METRICS = {
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
            "average": 50000,
            "min": 16000,
            "max": 10000,
        },
        "number_of_administrators": {
            "average": 5,
            "min": 10,
            "max": 3,
        },
        "time_to_implement_updates": {
            "average": 50,
            "min": 30.5,
            "max": 20,
        }
    }
}

PROCESS_FEW_TARGET_METRICS = {
    "target_metrics": {
        "number_of_lines_of_source_code_loc": {
           "average": 50,
           "min": 30.5,
           "max": 20,
        },
        "number_of_administrators": {
           "average": 50,
           "max": 20,
        }
    }
}

PROCESS_NO_TARGET_METRICS = {
    "target_metrics": {}
}

# helper data

PROCESS_ACTUAL_METRICS_ALL_ALL = {
    'number_of_lines_of_source_code_loc': [20000, 12000],
    'number_of_administrators': [10, 12],
    'time_to_implement_updates': [5, 3]
}

PROCESS_ACTUAL_METRICS_ALL_1_FEW = {
    'number_of_lines_of_source_code_loc': [20000, 5000],
    'number_of_administrators': [10],
    'time_to_implement_updates': [5]
}
