from flask import request, json , make_response
from utils.constants import ROOM_NAME_REQUIRED , ROOM_ENDPOINT , HTTP_400_BAD_REQUEST , USER_ID_MISSING_ERROR , ADD_MEMBER_ENDPOINT , ROOM_ID_MISSING_ERROR , ROOM_EXISTS_ERROR
from database.repositories.rooms_repository import RoomsRepository

def create_room_middleware():
    if request.endpoint == ROOM_ENDPOINT:
        body = json.loads(request.data)
        roomname = body['roomname']
        userId = body['userId']
        existing_room = RoomsRepository().find_one({'roomname': roomname})
        if existing_room:
            return make_response({'message': ROOM_EXISTS_ERROR}, HTTP_400_BAD_REQUEST)
        
        if not roomname:
            return make_response({'message': ROOM_NAME_REQUIRED}, HTTP_400_BAD_REQUEST)
        if not userId:
            return make_response({'message': USER_ID_MISSING_ERROR}, HTTP_400_BAD_REQUEST)
        
        
def add_member_middleware():
    if request.endpoint == ADD_MEMBER_ENDPOINT:
        body = json.loads(request.data)
        userId = body['userId']
        roomId = body['roomId']
        if not userId:
            return make_response({'message': USER_ID_MISSING_ERROR}, HTTP_400_BAD_REQUEST)
        if not roomId:
            return make_response({'message': ROOM_ID_MISSING_ERROR}, HTTP_400_BAD_REQUEST)

