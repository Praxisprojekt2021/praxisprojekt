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
# add a single component
# Frontend -> Backend -> Database
data = {
    "id": -1,  # wichtig -> als Indikator, dass neu angelegt und daher kein update sondern create
    "name": "SQL Datenbank",
    "category": "Datenbank",
    "description": "Datenbank zu xy mit ...",
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

# ----------------------------------------------------------------------------------------------------------------------
# view process list
# Database -> Backend -> Frontend
data = {
    "success": True,
    "process": [
        {
            "id": 1,
            "name": "Kunde anlegen",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            # erst ab Backend nach Risk calc
            "viv_score": 80,
        },
        {
            "id": 2,
            "name": "Kunde löschen",
            "creation_timestamp": "20210209...",
            "last_timestamp": "20210210...",
            # erst ab Backend nach Risk calc
            "viv_score": 40,
        }
        # ...
    ]
}

# -----------------------
# delete process
# Frontend -> Backend -> Database
data = {
    "id": 1,
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# view process
# Frontend -> Backend -> Database
data = {
    "id": 125,
}

# Database -> Backend -> Frontend
data = {
    "success": True,
    "process": {
        "id": 125,
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
        "components": [
            {
                "id": 1,
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
                "id": 3,
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
                "id": 2,
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
    "should-metrics": {
        "codelines": 25000,
        "admins": 12,
        "recovery_time": 3,
        # ...
    },
    # ab jetzt erst ab Backend durch Risk calc
    "viv_score": 80,  # percent as integer
    "is_metrics": {
        "codelines": [True, 30],  # true means that the metric is fine --> no problem.
        "admins": [True, 30],
        "recovery_time": [False, 20]  # false means that the metric is not fine --> problem.
    },
    "is_features": {
        "availability": True,
        "testability": False,
    }
}

# -----------------------------------------------------------

# Bei jeder Änderung wird an das Frontend das Prozess anzeigen JSON geschickt (über den entsprechenden Edit-Endpoint)

# create process or edit process data
# Frontend -> Backend -> Database
data = {
    "process": {
        "id": -1,  # when -1 it indicates that it is a new process, anything else indicates its an update
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
    },
    "should-metrics":
        {
            "codelines": 25000,
            "admins": 12,
            "recovery_time": 3,
            # ...
        }
}

# Database -> Backend
data = {
    "success": True,
}

# Backend -> Frontend
""" Prozess anzeigen JSON"""

# -----------------------
# delete process
# Frontend -> Backend -> Database
data = {
    "id": 125,  # process id not component id
    "weight": 2
}

# Database -> Backend
data = {
    "success": True
}

# Backend -> Frontend
""" Prozess anzeigen JSON"""

# -----------------------
# edit process step
# Frontend -> Backend -> Database
data = {
    "id": 125,  # process id not component id
    "old_weight": 3,
    "new_weight": 2.5
}

# Database -> Backend
data = {
    "success": True
}

# Backend -> Frontend
""" Prozess anzeigen JSON"""

# -----------------------
# create process step
# Frontend -> Backend -> Database
data = {
    "process_id": 125,
    "component_id": 126,
    "weight": 2.5
}

# Database -> Backend
data = {
    "success": True
}

# Backend -> Frontend
""" Prozess anzeigen JSON"""

# --------------------------------------------------------
# calculation risk
# Backend Core -> Backend Processing
data = {
    "success": True,
    "process": {
        "id": 111,
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
        "creation_timestamp": "20210210...",
        "last_timestamp": "20200211...",
        "components": [
            {
                "id": 12,
                "weight": 1,  # different from single component view!
                "name": "SQL Datenbank",
                "category": "Datenbank",
                "description": "Kundendatenbank",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": [
                    {"codelines": 20000},
                    {"admins": 10},
                    {"recovery_time": 5},
                    # ...
                ]
            },
            {
                "id": 3,
                "weight": 1.5,
                "name": "Frontend API",
                "category": "API",
                "description": "API für das Frontend",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": [
                    {"codelines": 20000},
                    {"admins": 10},
                    {"recovery_time": 5},
                    # ...
                ]
            },
            {
                "id": 2,
                "weight": 2,
                "name": "Hadoop Cluster",
                "category": "Datenbank",
                "description": "Big Data Plattform",
                "creation_timestamp": "20200219...",
                "last_timestamp": "20200219...",
                "metrics": [
                    {"codelines": 20000},
                    {"admins": 10},
                    {"recovery_time": 5},
                    # ...
                ]
            }
            # ...
        ]
    },
    "should-metrics": {
        "codelines": 25000,
        "admins": 12,
        "recovery_time": 3,
        # ...
    }
}

# Backend Processing -> Backend Core
data = {
    "viv_score": 80,  # percent as integer
    "is_metrics": {
        "codelines": [True, 30],  # true means that the metric is fine --> no problem.
        "admins": [True, 30],
        "recovery_time": [False, 20]  # false means that the metric is not fine --> problem.
    },
    "is_features": {
        "availability": True,
        "testability": False,
    }
}
