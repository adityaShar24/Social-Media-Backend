from flask import request , make_response , json
from utils.constants import USERNAME_MISSING_ERROR , HTTP_400_BAD_REQUEST , PASSWORD_MISSING_ERROR , EXISITING_USERNAME_ERROR , USER_NOT_EXISTS_ERROR , REGISTER_USER_ENDPOINT , LOGIN_USER_ENDPOINT , USER_ID_MISSING_ERROR , MAKE_REQUEST_ENDPOINT , REQUEST_ID_MISSING_ERROR ,REMOVE_REQUEST_ENDPOINT
from models.user_model import User
from models.make_request_model import Request


def register_user_middleware():
    if request.endpoint == REGISTER_USER_ENDPOINT:
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        
        if not username:
            return make_response({'message': USERNAME_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({'message':PASSWORD_MISSING_ERROR } , HTTP_400_BAD_REQUEST)
                
        existing_user = User.find_by_username(username)
        
        if existing_user:
            return make_response({'message':EXISITING_USERNAME_ERROR} , HTTP_400_BAD_REQUEST)
    
    
def login_user_middleware():
    if request.endpoint == LOGIN_USER_ENDPOINT:
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        
        if not username:
            return make_response({'message': USERNAME_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({'message':PASSWORD_MISSING_ERROR } , HTTP_400_BAD_REQUEST)
        
        existing_user = User.find_by_username(username)
        
        if not existing_user:
            return make_response({'message': USER_NOT_EXISTS_ERROR.format(username = username)} , HTTP_400_BAD_REQUEST)

        
def make_request_middleware():
    if request.endpoint == MAKE_REQUEST_ENDPOINT:
        body = json.loads(request.data)
        From = body['From']
        to = body['to']
                
        if not From:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not to:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    
def remove_friend_request_middleware():
    if request.endpoint == REMOVE_REQUEST_ENDPOINT:
        body = json.loads(request.data)
        
        request_id = body['request_id']
        
        if not request_id:
            return make_response({'message': REQUEST_ID_MISSING_ERROR})
