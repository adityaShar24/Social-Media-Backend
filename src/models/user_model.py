from database.mongo import users_collection
from bson.objectid import ObjectId

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.request_sent = []
        self.request_received = []
        self.friends = []
    
    def add_request_id(From , to  , request_id):
        fromUser = users_collection.update_one({ "_id": ObjectId(From) }, { "$push": { "request_sent": request_id } })
        toUser = users_collection.update_one({ "_id": ObjectId(to) }, { "$push": { "request_received": request_id } })

    def remove_request_id(From , to , request_id):
        fromUser = users_collection.update_one({ "_id": ObjectId(From) }, { "$pull": { "request_sent": request_id } })
        toUser = users_collection.update_one({ "_id": ObjectId(to) }, { "$pull": { "request_received": request_id } })

        
    def save_user(self):
        user_id = users_collection.insert_one({'username':self.username , 'password':self.password , 'friends': self.friends , 'request_sent': self.request_sent , 'request_received':self.request_received}).inserted_id
        return user_id
    
    def find_by_username(username):
        user = users_collection.find_one({'username':username})
        return user
    
