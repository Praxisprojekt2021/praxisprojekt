ADD_COMPONENT_IN = {
    "uid": "-1",
    "name": "SQL Datenbank",
    "category": "databases",
    "description": "Datenbank zu xy mit ...",
    "metrics": {
        "number_of_lines_of_source_code_loc": 20000,
        "number_of_administrators": 10,
        "restore_time": 5,
    }
}

GET_COMPONENT_IN = {
    "uid": "",
}

# Database -> Backend -> Frontend
GET_COMPONENT_OUT = {
    "success": True,
    "component": {
        "uid": "",
        "name": "SQL Datenbank",
        "category": "databases",
        "description": "Datenbank zu xy mit ...",
        "metrics": {
            "number_of_lines_of_source_code_loc": 20000,
            "number_of_administrators": 10,
            "restore_time": 5,
        }
    }
}
