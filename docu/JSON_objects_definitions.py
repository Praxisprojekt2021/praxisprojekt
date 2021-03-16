"""
File containing definitions of JSON objects for exchange between database, backend and frontend
"""

# error
# Database -> Backend -> Frontend
data = {
    "success": False,
}
# -----------------------
# view component list
# Database -> Backend -> Frontend
data = {
    "success": True,
    "components": [
        {"id": 1,
         "name": "SQL Datenbank",
         "category": "Datenbank",
         "creation_timestamp": "20200219...",
         "last_timestamp": "20200219...",
         },
        {"id": 2,
         "name": "Oracle Datenbank",
         "category": "Datenbank",
         "creation_timestamp": "20200219...",
         "last_timestamp": "20200219...",
         }
        # ...
    ]
}

# -----------------------
# get single component
# Frontend -> Backend -> Database
data = {
    "id": 1,
}

# Database -> Backend -> Frontend
data = {
    "success": True,
    "id": 1,
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Datenbank zu xy mit ...",
    "creation_timestamp": "20200219...",
    "last_timestamp": "20200219...",
    "metrics": {
        "codelines": 20000,
        "admins": 10,
        "recovery_time": 5,
        # ...
    },
}

# -----------------------
# edit single component
# Frontend -> Backend -> Database
data = {
    "id": 1,
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Datenbank zu xy mit ...",
    "creation_timestamp": "20200219...",
    "last_timestamp": "20200219...",
    "metrics": {
        "codelines": 20000,
        "admins": 10,
        "recovery_time": 5,
    },
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# delete single component
# Frontend -> Backend -> Database
data = {
    "id": 1,
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# create a single component
# Frontend -> Backend -> Database
data = {
    "id": 0,    # wichtig -> als Indikator, dass neu angelegt und daher kein update sondern create
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Datenbank zu xy mit ...",
    "creation_timestamp": "20200219...",
    "last_timestamp": "20200219...",
    "metrics": {
        "codelines": 20000,
        "admins": 10,
        "recovery_time": 5,
    },
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}
