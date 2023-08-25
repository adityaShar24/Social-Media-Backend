from flask import request , json , make_response
from models.user_model import User
from utils.constants import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , USER_REGISTERED_MESSAGE
import bson.json_util as json_util

def register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    user = User(username , password)
    saved_users = user.save_user()
    json_version = json_util.dumps(saved_users)
    return make_response({'message': USER_REGISTERED_MESSAGE.format(username), 'user': json_version} , HTTP_201_CREATED)