schema = {
    'bsonType': 'object',
    'required': ['message', 'roomId', 'userId'],
    'properties': {
        'message': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'roomId': {
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        },
        'userId': {
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        }
    }
}