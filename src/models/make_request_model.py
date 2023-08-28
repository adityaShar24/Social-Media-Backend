from bson.objectid import ObjectId
from database.mongo import request_collection

class Request:
    def __init__(self, userId , status = "pending"):
        self.From = ObjectId(userId)
        self.to = ObjectId(userId)
        self.status = status
    
    def make_request(self):
        request_id = request_collection.insert_one({'from':self.From , 'to': self.to , 'status': self.status}).inserted_id
        return request_id
    
    
    