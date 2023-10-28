from flask import request , make_response , json
from utils.constants import HTTP_400_BAD_REQUEST ,  USER_ID_MISSING_ERROR , MAKE_REQUEST_ENDPOINT , REQUEST_ID_MISSING_ERROR ,REMOVE_REQUEST_ENDPOINT , RESPONSE_REQUEST_ENDPOINT 


def make_request_middleware():
    if request.endpoint == MAKE_REQUEST_ENDPOINT:
        body = json.loads(request.data)
        sender = body['sender']
        receiver = body['receiver']
                
        if not sender:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not receiver:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    
def remove_friend_request_middleware():
    if request.endpoint == REMOVE_REQUEST_ENDPOINT:
        body = json.loads(request.data)
        
        request_id = body['request_id']
        
        if not request_id:
            return make_response({'message': REQUEST_ID_MISSING_ERROR})

def accept_request_middleware():
    if request.endpoint == RESPONSE_REQUEST_ENDPOINT:
        body = json.loads(request.data)
        
        request_id = body['request_id']
        
        if not request_id:
            return make_response({'message': REQUEST_ID_MISSING_ERROR})
        
def reject_request_middleware():
    if request.endpoint == RESPONSE_REQUEST_ENDPOINT:
        body = json.loads(request.data)
        
        request_id = body['request_id']
        
        if not request_id:
            return make_response({'message': REQUEST_ID_MISSING_ERROR})
