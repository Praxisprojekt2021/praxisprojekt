PROCESS_WITHOUT_TARGET_METRICS = {
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

UID_DICT = {
    "uid": "",
}

ADD_PROCESS_REFERENCE = {
    "process_uid": "-1",
    "component_uid": "-1",
    "weight": 69
}

UPDATE_PROCESS_REFERENCE = {
    "uid": "-1",
    "old_weight": 69,
    "new_weight": 7
}

PROCESS_WITH_TARGET_METRICS = {
    'success': True,
    'process':
        {
            'uid': 'f4ad455843da4c448b607ebe0d01d85b',
            'responsible_person': 'Peter Rossbach',
            'name': 'Kunde anlegen',
            'description': 'Prozess zum anlegen von einem neuen Kunden in allen Systemen',
            'components':
                [{
                    'uid': '244ee95d17ae4f83b921c0b720cfa7e7',
                    'name': 'SQL Datenbank',
                    'description': 'Datenbank zu xy mit ...',
                    'category': 'databases',
                    'metrics': {
                        'restore_time': 5.0,
                        'number_of_administrators': 10.0,
                        'number_of_lines_of_source_code_loc': 20000.0},
                    'weight': 69
                }]
        },
    'target_metrics': {
        'downtime': {
            'average': 50.0, 'min': 30.5, 'max': 20.0
        },
        'comment_quality': {
            'average': 50.0, 'min': 30.5, 'max': 20.0
        }
    }
}
