schema = {
    'bsonType': 'object',
    'required': ['username', 'password'],
    'properties': {
        'username': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'password': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'friends': {
            'bsonType': 'array',
            'description': 'must be a array'
        },
        'request_sent': {
            'bsonType': 'array',
            'description': 'must be a array'
        },
        'request_received': {
            'bsonType': 'array',
            'description': 'must be a array'
        },
        'posts': {
            'bsonType': 'array',
            'description': 'must be a array'
        },
        'saved_posts': {
            'bsonType': 'array',
            'description': 'must be a array'
        }
    }
}

