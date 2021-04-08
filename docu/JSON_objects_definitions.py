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
        {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
         "name": "SQL Datenbank",
         "category": "Datenbank",
         "creation_timestamp": "20200219...",
         "last_timestamp": "20200219...",
         },
        {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
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
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
    "success": True,
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
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
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
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
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# add a single component
# Frontend -> Backend -> Database
data = {
    "uid": -1,  # wichtig -> als Indikator, dass neu angelegt und daher kein update sondern create
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
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde anlegen",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            # erst ab Backend nach Risk calc
            "score": 80,
            "components_count": 4,
        },
        {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde löschen",
            "creation_timestamp": "20210209...",
            "last_timestamp": "20210210...",
            # erst ab Backend nach Risk calc
            "score": 40,
            "components_count": 15,
        }
        # ...
    ]
}

# -----------------------
# delete process
# Frontend -> Backend -> Database
data = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# view process
# Frontend -> Backend -> Database
data = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
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
    # nach risk calc dann nicht mehr drin
    "target_metrics": {
        "codelines": 25000,
        "admins": 12,
        "recovery_time": 3,
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
            "component_count": 10,
            "fulfillment": True
        },  # true means that the metric is fulfilled --> no problem.
        "number_of_administrators": {
            "actual": {
                "average": 30,
                "max": 50,
                "min": 20,
                "standard_deviation": 5,
                "total": 300,     # summe
            },
            "target": {
                "average": 30,
                "total": 300,     # summe
            },
            "component_count": 10,
            "fulfillment": True
        },
        "recovery_time": {
            "actual": {
                "average": 0.65,
                "max": 0.8,
                "min": 0.5,
                "standard_deviation": 5,
                "total": 0.4,     # summe
            },
            "target": {
                "average": 0.8,
                "total": 0.64,     # summe
            },
            "component_count": 2,
            "fulfillment": True
        },  # false means that the metric is not fulfilled --> problem.
    }
}

# -----------------------------------------------------------

# Bei jeder Änderung wird an das Frontend das Prozess anzeigen JSON geschickt (über den entsprechenden Edit-Endpoint)

# create process or edit process data
# Frontend -> Backend -> Database
data = {
    "process": {
        "uid": -1,  # when -1 it indicates that it is a new process, anything else indicates its an update
        "name": "Kunde anlegen",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
    },
    "target_metrics":{
        "codelines": 25000,
        "admins": 12,
        "recovery_time": 3,
        # ...
    }
}

# Database -> Backend 
# process uid only create: uid is needed to directly return the process view JSON
data = {
    "success": True,
    "process_uid": "b141f94973a43cf8ee972e9dffc1b004"  
}

# Backend -> Frontend
""" Prozess anzeigen JSON"""

# -----------------------
# delete process step
# Frontend -> Backend -> Database
data = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",  # process uid not component uid
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
    "uid": "b141f94973a43cf8ee972e9dffc1b004",  # process uid not component uid
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
    "process_uid": "b141f94973a43cf8ee972e9dffc1b004",
    "component_uid": "b141f94973a43cf8ee972e9dffc1b005",
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
                "metrics":  {
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
        "codelines": 25000,
        "admins": 12,
        "recovery_time": 3,
        # ...
    }
}

# Backend Processing -> Backend Core
data = {
    "score": 80,  # percent as integer
    "actual_target_metrics": {
        "codelines": {
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
            "component_count": 10,
            "fulfillment": True
        },  # true means that the metric is fulfilled --> no problem.
        "admins": {
            "actual": {
                "average": 30,
                "max": 50,
                "min": 20,
                "standard_deviation": 5,
                "total": 300,     # summe
            },
            "target": {
                "average": 30,
                "total": 300,     # summe
            },
            "component_count": 10,
            "fulfillment": True
        },
        "recovery_time": {
            "actual": {
                "average": 0.65,
                "max": 0.8,
                "min": 0.5,
                "standard_deviation": 5,
                "total": 0.4,     # summe
            },
            "target": {
                "average": 0.8,
                "total": 0.64,     # summe
            },
            "component_count": 2,
            "fulfillment": True
        },  # false means that the metric is not fulfilled --> problem.
    }
}
