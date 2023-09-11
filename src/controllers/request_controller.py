from flask import request , json , make_response
from models.user_model import User
from models.make_request_model import Request
from database.mongo import request_collection
from utils.constants import HTTP_201_CREATED ,  REQUEST_SENT_MESSAGE , REQUEST_DELETED_MESSAGE , REQUEST_ACCEPTED_MESSAGE , REJECT_REQUEST_MESSAGE
import bson.json_util as json_util
from bson.objectid import ObjectId

def make_request():
    body = json.loads(request.data)
    From = body['From']
    to = body['to']
    
    request_instance = Request(From , to)
    request_id = request_instance.make_request()
    
    user_make_request = User.add_request_id(From , to , request_id)
    
    json_verison = json_util.dumps(request_id)
    return make_response({'message':REQUEST_SENT_MESSAGE , "request": json_verison } , HTTP_201_CREATED)
    
def remove_request():
    body = json.loads(request.data)
    request_id = body["request_id"]
    
    request_doc = request_collection.find_one({"_id": ObjectId(request_id)})
    
    User.remove_request_id(request_doc['from'] , request_doc['to'] ,  ObjectId(request_id))
    request_collection.find_one_and_delete({ "_id":  ObjectId(request_id) })
    
    return make_response({'message': REQUEST_DELETED_MESSAGE} , HTTP_201_CREATED)
    
    
def accept_request():
    body = json.loads(request.data)
    request_id = body["request_id"]
    
    Request.accept_request(request_id)
    
    return make_response({"message": REQUEST_ACCEPTED_MESSAGE} , HTTP_201_CREATED)


def reject_request():
    body = json.loads(request.data)
    request_id = body["request_id"]

    Request.reject_request(request_id)
    
    return make_response({'message': REJECT_REQUEST_MESSAGE} , HTTP_201_CREATED)
