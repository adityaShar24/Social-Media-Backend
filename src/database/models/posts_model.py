schema = {
    'bsonType': 'object',
    'required': ['url', 'caption', 'userId'],
    'properties': {
        'url': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'caption': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'userId': {
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        },
        'likes': {
            'bsonType': 'int',
            'description': 'must be a string and is required'
        },
        'comments': {
            'bsonType': 'array',
            'description': 'must be a string and is required'
        }
    }
}