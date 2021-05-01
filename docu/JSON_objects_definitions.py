"""
File containing definitions of JSON objects for exchange between database, backend and frontend
"""

# Error
# Database -> Backend -> Frontend
data = {
    "success": False,
}

# -----------------------
# get_component_list
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
# get_component
# Frontend -> Backend -> Database
data = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
    "success": True,
    "component": {
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
        }
    }
}

# -----------------------
# update_component
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
# delete_component
# Frontend -> Backend -> Database
data = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# add_component
# Frontend -> Backend -> Database
data = {
    "uid": "-1",  # wichtig -> als Indikator, dass neu angelegt und daher kein update sondern create
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
# get_process_list
# Database -> Backend -> Frontend
data = {
    "success": True,
    "processes": [
        {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde anlegen",
            "responsible_person": "Peter Rossbach",
            "creation_timestamp": "20210210...",
            "last_timestamp": "20200211...",
            # erst ab Backend nach Risk calc
            "score": 80,
            "components_count": 4,
        },
        {
            "uid": "b141f94973a43cf8ee972e9dffc1b004",
            "name": "Kunde löschen",
            "responsible_person": "Peter Rossbach",
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
# delete_process
# Frontend -> Backend -> Database
data = {
    "uid": "b141f94973a43cf8ee972e9dffc1b004",
}

# Database -> Backend -> Frontend
data = {
    "success": True,
}

# -----------------------
# get_process
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
        "codelines": {
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
        "recovery_time": {
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

# -----------------------------------------------------------
# Bei jeder Änderung wird an das Frontend das Prozess anzeigen JSON geschickt (über den entsprechenden Edit-Endpoint)

# create_process or update_process
# Frontend -> Backend -> Database
data = {
    "process": {
        "uid": "-1",  # when -1 it indicates that it is a new process, anything else indicates its an update
        "name": "Kunde anlegen",
        "responsible_person": "Peter Rossbach",
        "description": "Prozess zum anlegen von einem neuen Kunden in allen Systemen",
    },
    "target_metrics": {
        "codelines": {
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

# Database -> Backend
# process uid only create: uid is needed to directly return the process view JSON
data = {
    "success": True,
    "process_uid": "b141f94973a43cf8ee972e9dffc1b004"
}

# Backend -> Frontend
""" Prozess anzeigen JSON"""

# -----------------------
# delete_process_reference
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
# update_process_reference
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
# add_process_reference
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
    "target_metrics": {
        "codelines": {
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


# metric_handler.get_metrics_data -> core -> calculations

data = {
    'success': True,
    'metrics': {
        'automation': {
            'uid': 'd0cfbd93a0d146d9a223b7cfad098a7a',
            'fulfilled_if': '>'
        },
        'test_automation': {
            'uid': '1de621af9cb7404291a55671463b5ad7',
            'fulfilled_if': '>'
        },
        'ratio_of_late_corrections': {
            'uid': '3197d7334db748189d01dc43e60137a5',
            'fulfilled_if': '>'
        },
        'pre_post_release_faults_ratio': {
            'uid': '829e81d56e3c4b76b545b65537fa7e95',
            'fulfilled_if': '>'
        },
        'error_during_testing': {
            'uid': 'a6bc173d9e2649899568698c23c187a9',
            'fulfilled_if': '>'
        },
        'testability': {
            'uid': '9ae1ea37923c470abf215297a7e9b2f5',
            'fulfilled_if': '>'
        },
        'restore_time': {
            'uid': '5e655b8ca216431baa0b616dc510795b',
            'fulfilled_if': '<'
        },
        'downtime': {
            'uid': '3912b00a4648487b90c92adb15304977',
            'fulfilled_if': '<'
        },
        'planned_maintenance_percentage': {
            'uid': '33780b041560450cb498b27a8bee954f',
            'fulfilled_if': '<'
        },
        'redundancy': {
            'uid': '4f5b983da6554dc78e714c511cac1777',
            'fulfilled_if': '>'
        },
        'number_of_administrators': {
            'uid': 'a8d19d183dec4dd5bd59924d64879e25',
            'fulfilled_if': '>'
        },
        'encryption': {
            'uid': '718dc5e3724d462e8c0fe97e665626a5',
            'fulfilled_if': '>'
        },
        'time_between_failures': {
            'uid': '5450970b267744ab94cd1984b7d9df5c',
            'fulfilled_if': '>'
        },
        'maximum_downtime_at_a_time': {
            'uid': '43cf04efc71043499edaa4231bea2dae',
            'fulfilled_if': '<'
        },
        'number_of_lines_of_source_code_loc': {
            'uid': 'b30a6d26c6134c07b3b8439662977632',
            'fulfilled_if': '<'
        },
        'development_time': {
            'uid': '541dd00f31f543b4b57d31e39e7512f9',
            'fulfilled_if': '<'
        },
        'code_review_frequency': {
            'uid': 'd9da830bdf434963b965e62032fba383',
            'fulfilled_if': '>'
        },
        'comment_quality': {
            'uid': 'd049296893d54e138ccf095d8617515d',
            'fulfilled_if': '>'
        },
        'back-up': {
            'uid': '202e39d1fdae4a8cbbf3d625ab2c379f',
            'fulfilled_if': '>'
        },
        'test_scope': {
            'uid': 'e4d6f7372dda4c3bad0c4e2414d8d7f3',
            'fulfilled_if': '>'
        },
        'change_tracking': {
            'uid': '5b0eee6edb08446ca7329b66dc17d751',
            'fulfilled_if': '>'
        },
        'complaints': {
            'uid': '9870746c577946c8ba33526711fd22e1',
            'fulfilled_if': '<'
        },
        'patch_status_check': {
            'uid': 'a4947283abe747788c896df63d1451a4',
'           fulfilled_if': '>'
        },
        'training': {
            'uid': 'acbce74d1cb14230b55d95a7d84552a2',
            'fulfilled_if': '>'
        },
        'time_to_implement_updates': {
            'uid': '0fe49270553147b286796fc4a9af7ae7',
            'fulfilled_if': '<'
        },
        'external_support': {
            'uid': 'b6fe9cae2b774b24ba9a8b574bc02aef',
            'fulfilled_if': '>'
        },
        'internal_support': {
            'uid': 'c3c133eb49f846fab0496e36dfa545e7',
            'fulfilled_if': '>'
        },
        'number_of_views_per_day': {
            'uid': 'eee796fd75a5425e87d7e4d8e329c30a',
            'fulfilled_if': '<'
        },
        'restart': {
            'uid': '521295b3c71740cd8ba2d46a1afaf201',
            'fulfilled_if': '<'
        }
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
        "recovery_time": {
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
