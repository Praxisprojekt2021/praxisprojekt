GET_COMPONENT_LIST_OUT = {
    "success": True,
    "components": [
        {
            "uid": "",
            "name": "SQL Datenbank",
            "description": "Datenbank zu xy mit ...",
            "category": "databases",
        },
        {
            "uid": "",
            "name": "SQL Datenbank",
            "description": "Datenbank zu xy mit ...",
            "category": "databases",
        },
        {
            "uid": "",
            "name": "SQL Datenbank",
            "description": "Datenbank zu xy mit ...",
            "category": "databases",
        }
    ]
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

ADD_COMPONENT_OUT = {
    "success": True,
}

UPDATE_COMPONENT_IN = {
    "uid": "",
    "name": "SQL Datenbank",
    "category": "databases",
    "description": "Datenbank zu xy mit ...",
    "metrics": {
        "number_of_lines_of_source_code_loc": 40000,
        "number_of_administrators": 20,
        "restore_time": 95,
    }
}

UPDATE_COMPONENT_OUT = {
    "success": True,
}

DELETE_COMPONENT_IN = {
    "uid": "",
}

DELETE_COMPONENT_OUT = {
    "success": True,
}
