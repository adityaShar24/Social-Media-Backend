from flask import request , make_response , json
from utils.constants import USERNAME_MISSING_ERROR , HTTP_400_BAD_REQUEST , PASSWORD_MISSING_ERROR , EXISITING_USER_ERROR
from models.user_model import User


def register_user_middleware():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    
    if not username:
        return make_response({'message': USERNAME_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
    
    if not password:
        return make_response({'message':PASSWORD_MISSING_ERROR } , HTTP_400_BAD_REQUEST)
    
    user = User(username , password)
    
    existing_user = user.find_by_username(username)
    
    if existing_user:
        return make_response({'message':EXISITING_USER_ERROR} , HTTP_400_BAD_REQUEST)
    