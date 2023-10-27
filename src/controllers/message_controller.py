from flask import json , request , make_response
import bson.json_util as json_uitl
from database.repositories.message_repository import MessagesRepository
from utils.constants import HTTP_201_CREATED , MESSAGE_SENT , MESSAGE_DELETED 
from flask_socketio import emit
from bson.objectid import ObjectId


def send_message():
    body = json.loads(request.data)
    userId = body['userId']
    roomId = body['roomId']
    content = body['content']
    
    emit("message",{"userID":userId,"roomId":roomId,"content":content}, broadcast=True ,to=roomId , namespace='/') 
    
    messageId = MessagesRepository().create({"userId":userId,"roomId":roomId,"content":content})
    
    json_version = json_uitl.dumps(messageId)
    return make_response({'message': MESSAGE_SENT , 'data':json_version} , HTTP_201_CREATED)
    
def delete_message():
    messageId = request.args.get('messageId')
    
    MessagesRepository().find_one_and_delete({"_id":ObjectId(messageId)})
    
    return make_response({'message': MESSAGE_DELETED} , HTTP_201_CREATED)

def get_all_messages():
    roomId = request.args.get('roomId')
    
    messages = MessagesRepository().find_one({"roomId":ObjectId(roomId)})
    list_messages = list(messages)
    
    json_version = json_uitl.dumps(list_messages)
    return make_response({'data':json_version} , HTTP_201_CREATED)
    
    