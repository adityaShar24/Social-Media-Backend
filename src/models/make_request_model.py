from bson.objectid import ObjectId
from database.mongo import request_collection

class Request:
    def __init__(self, userId1 , userId2 , status = "pending"):
        self.From = ObjectId(userId1)
        self.to = ObjectId(userId2)
        self.status = status
    
    def make_request(self):
        request_id = request_collection.insert_one({'from':self.From , 'to': self.to , 'status': self.status}).inserted_id
        return request_id
    
    def accept_request(request_id):
        find_request = request_collection.find_one({"_id": ObjectId(request_id)})
        
        update_to_accepted = request_collection.update_one(
            {"_id":request_id} , 
            { "$set" : { "status" : "accepted"}}
        )
        
        
        
    
    