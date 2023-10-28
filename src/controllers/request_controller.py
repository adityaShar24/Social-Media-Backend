from flask import request , json , make_response
from database.repositories.user_repository import UserRepository
from database.repositories.request_repository import RequestsRepository
from database.mongo import request_collection
from utils.constants import HTTP_201_CREATED ,  REQUEST_SENT_MESSAGE , REQUEST_DELETED_MESSAGE , REQUEST_ACCEPTED_MESSAGE , REJECT_REQUEST_MESSAGE
import bson.json_util as json_util
from bson.objectid import ObjectId

def make_request():
    body = json.loads(request.data)
    sender = body['sender']
    receiver = body['receiver']
    
    request_id = RequestsRepository().create({'sender': ObjectId(sender) , 'receiver': ObjectId(receiver)})
    UserRepository().update_one({"_id": ObjectId(sender) }, { "$push": { "requests": ObjectId(request_id) } })
    
    json_verison = json_util.dumps(request_id)
    return make_response({'message':REQUEST_SENT_MESSAGE , "request": json_verison } , HTTP_201_CREATED)
    
    
    
def accept_request():
    body = json.loads(request.data)
    request_id = body["request_id"]
    
    UserRepository().update_one(
        {"_id":ObjectId(request_id)} , 
        {"$set" : { 'status' : "accepted"}}
    )

    request = RequestsRepository().find_one({"_id": ObjectId(request_id)})
    
    if request:
        UserRepository().update_one({"_id": ObjectId(request['sender'])}, { "$push": { "friends": request['receiver'] } })
        UserRepository().update_one({"_id": ObjectId(request['receiver'])}, {"$push": {"friends": request['sender']}} )

    
    return make_response({"message": REQUEST_ACCEPTED_MESSAGE} , HTTP_201_CREATED)


def reject_request():
    body = json.loads(request.data)
    request_id = body["request_id"]

    RequestsRepository.update_one(
        {"_id":ObjectId(request_id)} , 
        {"$set": {'status':'rejected'}}
        )

    
    return make_response({'message': REJECT_REQUEST_MESSAGE} , HTTP_201_CREATED)


def remove_request():
    body = json.loads(request.data)
    request_id = body["request_id"]
    
    request_doc = request_collection.find_one({"_id": ObjectId(request_id)})
    
    fromUser = UserRepository().update_one({ "_id": ObjectId(request_doc['sender']) }, { "$pull": { "request_sent": request_id } })
    toUser = UserRepository().update_one({ "_id": ObjectId(request_doc['receiver']) }, { "$pull": { "request_received": request_id } })
    
    return make_response({'message': REQUEST_DELETED_MESSAGE} , HTTP_201_CREATED)
