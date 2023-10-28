schema = {
    'bsonType': 'object',
    'required': ['sender' , 'receiver'],
    'properties': {
        'sender': {
            'bsonType': 'objectId',
            'description': 'must be a objectId and is required'
        },
        'receiver': {
            'bsonType': 'objectId',
            'description': 'must be a objectId and is required'
        },
        'status': {
            'bsonType': 'string',
            'description': 'must be a string',
        }
    }
}
