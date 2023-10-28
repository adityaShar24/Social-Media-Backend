from flask import request , json , make_response
from utils.constants import MESSAGE_TEXT_REQUIRED , MESSAGE_ENDPOINT , HTTP_400_BAD_REQUEST , USER_ID_MISSING_ERROR , ROOM_ID_MISSING_ERROR

def send_message_middleware():
    if request.endpoint == MESSAGE_ENDPOINT:
        body = json.loads(request.data)
        userId = body['userId']
        roomId = body['roomId']
        content = body['content']
        
        if not userId:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not roomId:
            return make_response({'message': ROOM_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    
        if not content:
            return make_response({'message': MESSAGE_TEXT_REQUIRED} , HTTP_400_BAD_REQUEST)