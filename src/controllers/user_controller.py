from flask import request , json , make_response
from models.user_model import User
from models.make_request_model import Request
from flask_jwt_extended import create_access_token
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE , INVALID_PASSWORD_ERROR , REQUEST_SENT_MESSAGE
import bson.json_util as json_util
import datetime

def register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    user = User(username , password)
    saved_users = user.save_user()
    json_version = json_util.dumps(saved_users)
    return make_response({'message': USER_REGISTERED_MESSAGE.format(username = username), 'user': json_version} , HTTP_201_CREATED)

def login():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    user = User.find_by_username(username)
        
    if password != user['password']:
        return make_response({'message':INVALID_PASSWORD_ERROR} , HTTP_400_BAD_REQUEST)
    
    access_token = create_access_token(identity=username , fresh=datetime.timedelta(minutes=30))
    return make_response({'message':{'access token':access_token}} , HTTP_201_CREATED)


def make_request():
    body = json.loads(request.data)
    From = body['userID']
    to = body['userID']
    
    request = Request.make_request(From , to)
    json_version = json_util.dumps(request)
    return make_request({'message': REQUEST_SENT_MESSAGE , 'request': json_version} , HTTP_201_CREATED)