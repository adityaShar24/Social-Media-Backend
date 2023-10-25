from flask import request, json , make_response
from utils.constants import ROOM_NAME_REQUIRED , ROOM_ENDPOINT , HTTP_400_BAD_REQUEST , USER_ID_MISSING_ERROR
from database.repositories.rooms_repository import RoomsRepository

def create_room_middleware():
    if request.endpoint == ROOM_ENDPOINT:
        body = json.loads(request.data)
        roomname = body[roomname]
        userId = body[userId]
        if not roomname:
            return make_response({'message': ROOM_NAME_REQUIRED}, HTTP_400_BAD_REQUEST)
        if not userId:
            return make_response({'message': USER_ID_MISSING_ERROR}, HTTP_400_BAD_REQUEST)
        existing_room = RoomsRepository.find_one(roomname)
        

