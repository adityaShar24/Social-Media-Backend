schema = {
    'bsonType': 'object',
    'required': ['from' , 'to' , 'status'],
    'properties': {
        'from': {
            'bsonType': 'objectId',
            'description': 'must be a objectId and is required'
        },
        'to': {
            'bsonType': 'objectId',
            'description': 'must be a objectId and is required'
        },
        'status': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        }
    }
}
