from flask import request , make_response , json
from utils.constants import USERNAME_MISSING_ERROR , HTTP_400_BAD_REQUEST , PASSWORD_MISSING_ERROR , EXISITING_USERNAME_ERROR , USER_NOT_EXISTS_ERROR , REGISTER_USER_ENDPOINT , LOGIN_USER_ENDPOINT , USER_ID_MISSING_ERROR , MAKE_REQUEST_ENDPOINT , REQUEST_ID_MISSING_ERROR ,REMOVE_REQUEST_ENDPOINT , RESPONSE_REQUEST_ENDPOINT , ADD_POST_ENDPOINT
from database.repositories.user_repository import UserRepository

def register_user_middleware():
    if request.endpoint == REGISTER_USER_ENDPOINT:
        print(REGISTER_USER_ENDPOINT)
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        
        if not username:
            return make_response({'message': USERNAME_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not password:
            return make_response({'message':PASSWORD_MISSING_ERROR } , HTTP_400_BAD_REQUEST)
                
        existing_user = UserRepository().find_one({'username':username})
        
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
        
        existing_user = UserRepository().find_one({'username':username})
        
        if not existing_user:
            return make_response({'message': USER_NOT_EXISTS_ERROR.format(username = username)} , HTTP_400_BAD_REQUEST)

        
