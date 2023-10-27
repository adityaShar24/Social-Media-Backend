from flask import json , request , make_response
import bson.json_util as json_uitl
from database.repositories.message_repository import MessagesRepository
from utils.constants import HTTP_201_CREATED , MESSAGE_SENT 
from flask_socketio import emit


def send_message():
    body = json.loads(request.data)
    userId = body['userId']
    roomId = body['roomId']
    content = body['content']
    
    emit("message",{"userID":userId,"roomId":roomId,"content":content}, broadcast=True ,to=roomId , namespace='/') 
    
    message = MessagesRepository().create({"userId":userId,"roomId":roomId,"content":content})
    
    json_version = json_uitl.dumps(message)
    return make_response({'message': MESSAGE_SENT , 'data':json_version} , HTTP_201_CREATED)
    