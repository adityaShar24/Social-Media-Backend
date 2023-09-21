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
            'bsonType': 'objectId',
            'description': 'must be a string and is required'
        }
    }
}