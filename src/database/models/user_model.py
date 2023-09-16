from database.mongo import users_collection
from bson.objectid import ObjectId

# create the mongoDB validation schema for User
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

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.request_sent = []
        self.request_received = []
        self.friends = []
        self.posts = []
        self.saved_posts = []
    
    def add_request_id(From , to  , request_id):
        fromUser = users_collection.update_one({ "_id": ObjectId(From) }, { "$push": { "request_sent": request_id } })
        toUser = users_collection.update_one({ "_id": ObjectId(to) }, { "$push": { "request_received": request_id } })

    def remove_request_id(From , to , request_id):
        fromUser = users_collection.update_one({ "_id": ObjectId(From) }, { "$pull": { "request_sent": request_id } })
        toUser = users_collection.update_one({ "_id": ObjectId(to) }, { "$pull": { "request_received": request_id } })
                
    def save_user(self):
        user_id = users_collection.insert_one({
            'username':self.username , 
            'password':self.password , 
            'friends': self.friends , 
            'request_sent': self.request_sent , 
            'request_received':self.request_received , 
            'posts':self.posts , 
            'saved_posts': self.saved_posts,
            }).inserted_id
        return user_id
    
    def find_by_username(username):
        user = users_collection.find_one({'username':username})
        return user
    
    def find_all_users():
        users = users_collection.find()
        list_all_users = list(users)
        return list_all_users
    
