schema = {
    'bsonType': 'object',
    'required': ['comment', 'postId', 'userId'],
    'properties': {
        'comment': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'postId': {
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        },
        'userId': {
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        },
        'parent_commentId': {
            'oneOf': [
                {'bsonType': 'objectId'},
                {'bsonType': 'null'}
            ],
            'description': 'must be an objectId or null'
        }
    }
}
