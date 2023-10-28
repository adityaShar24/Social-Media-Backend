from flask import json , request , make_response
from database.repositories.rooms_repository import RoomsRepository
from utils.constants import HTTP_201_CREATED , ROOM_CREATED_MESSAGE , ROOM_FETCHED_MESSAGE , ROOM_MEMBER_ADDED_MESSAGE
import bson.json_util as json_util
from bson.objectid import ObjectId

def create_room():
    body = json.loads(request.data)
    roomname = body['roomname']
    userId = body['userId']
    
    roomID = RoomsRepository().create({'roomname': roomname , 'userId':ObjectId(userId) , 'members':[] })
    
    json_version = json_util.dumps(roomID)
    return make_response({'message': ROOM_CREATED_MESSAGE , "room": json_version} , HTTP_201_CREATED)
    
def add_member():
    body = json.loads(request.data)
    roomId = body['roomId']
    userId = body['userId']
    
    members = RoomsRepository().update_one({"_id":ObjectId(roomId)} , {"$push": {"members": userId} })
    
    json_version = json_util.dumps(members)
    
    return make_response({"message": ROOM_MEMBER_ADDED_MESSAGE , "members": json_version} , HTTP_201_CREATED)


def get_all_rooms():
    rooms = RoomsRepository().find_many()
    rooms_list = list(rooms)
    
    json_version = json_util.dumps(rooms_list)
    
    return make_response({"message": ROOM_FETCHED_MESSAGE , "rooms": json_version } , HTTP_201_CREATED)