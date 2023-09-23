from flask import request , json , make_response
from database.repositories.user_repository import UserRepository
from flask_jwt_extended import create_access_token
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE , INVALID_PASSWORD_ERROR 
import bson.json_util as json_util
import datetime

def register():
    body = json.loads(request.data)
    
    username = body['username']
    password = body['password']
    
    saved_user = UserRepository().create({'username':username , 'password':password})
    
    json_version = json_util.dumps(saved_user)
    
    return make_response({'message': USER_REGISTERED_MESSAGE.format(username = username), 'user': json_version} , HTTP_201_CREATED)

def login():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    
    user = UserRepository().find_one({'username':username})
        
    if password != user['password']:
        return make_response({'message':INVALID_PASSWORD_ERROR} , HTTP_400_BAD_REQUEST)
    
    access_token = create_access_token(identity=username , fresh=datetime.timedelta(minutes=30))
    
    return make_response({'message':{'access token':access_token}} , HTTP_201_CREATED)


def get_all_users():
    users = UserRepository().find_many()
    json_version = json_util.dumps(users)
    return make_response({'users':json_version} , HTTP_201_CREATED)