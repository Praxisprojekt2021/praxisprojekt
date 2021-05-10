GET_PROCESS_SETUP_AND_OUT = {
    "success": True,
    "process": {
        "uid": "-1",
        "name": "Kunde anlegen",
        "responsible_person": "Peter Rossbach",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "components": []
    },
    "target_metrics": {
        "downtime": {
            "average": 50,
            "min": 30.5,
            "max": 20,
        },
        "comment_quality": {
            "average": 50,
            "min": 30.5,
            "max": 20,
        },
        # ...
    },
}
dict_input_dict = {
    "process": {
        "uid": 3,
        "name": "---",
        "description": "...."
    },
    "target_metrics": {"number_of_lines_of_source_code_loc": {"average": "2", "min": "d", "max": "d"}}
}

GET_PROCESS_IN = {
    "uid": "",
}
