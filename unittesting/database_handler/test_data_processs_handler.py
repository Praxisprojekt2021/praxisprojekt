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

GET_PROCESS_IN = {
    "uid": "",
}

ADD_PROCESS_OUT = {
    "success": True,
    "uid": -1
}
