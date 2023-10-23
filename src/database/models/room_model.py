schema = {
    'bsonType': 'object',
    'required': ['roomname', 'userId' , 'members'],
    'properties': {
        'roomname': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'userId': {
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        },
        'members': {
            'bsonType': 'array',
            'description': 'must be an array and is required',
            'items': {
                'bsonType': 'objectId',
                'description': 'must be a string and is required'
            }
        },
    }
}