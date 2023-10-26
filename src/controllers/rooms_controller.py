from flask import json , request , make_response
from database.repositories.rooms_repository import RoomsRepository
from database.repositories.user_repository import UserRepository
from utils.constants import HTTP_201_CREATED , ROOM_CREATED_MESSAGE , ROOM_DELETED_MESSAGE , ROOM_MEMBER_ADDED_MESSAGE
import bson.json_util as json_util

def create_room():
    body = json.loads(request.data)
    roomname = body['roomname']
    userId = body['userId']
    
    roomID = RoomsRepository().create({'roomname': roomname , 'userId': userId , 'members':[] })
    
    json_version = json_util.dumps(roomID)
    return make_response({'message': ROOM_CREATED_MESSAGE , "room": json_version} , HTTP_201_CREATED)
    