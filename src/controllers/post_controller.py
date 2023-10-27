from flask import request , json , make_response
from database.repositories.user_repository import UserRepository
from database.repositories.post_repository import PostsRepository
from utils.constants import HTTP_201_CREATED , POST_UPLOADED_MESSAGE , POST_SAVED_MESSAGE, HTTP_400_BAD_REQUEST
import bson.json_util as json_util
from bson.objectid import ObjectId as Ob


def post():
    body = json.loads(request.data)
    
    url = body['url']
    caption = body['caption']
    userId = body['userId']
    
    user = UserRepository().find_one({"_id": Ob(userId)})
    if user is None:
        return make_response({'message': 'User not found'} , HTTP_400_BAD_REQUEST)
    
    postId = PostsRepository().create({'url':url , 'caption':caption , 'userId':Ob(userId)})
    UserRepository().update_one({"_id": Ob(userId) }, { "$push": { "posts": Ob(postId) } })
    
    return make_response({'message': POST_UPLOADED_MESSAGE, "postId":json_util.dumps(postId) } , HTTP_201_CREATED)

def save_post():
    body = json.loads(request.data)
    
    postId = body['postId']
    userId = body['userId']
    
    UserRepository().update_one({"_id": Ob(userId) }, { "$push": { "saved_posts": Ob(postId) } })
    
    return make_response({'message': POST_SAVED_MESSAGE} , HTTP_201_CREATED)