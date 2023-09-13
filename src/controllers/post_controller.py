from flask import request , json , make_response
from models.posts_model import Posts
from utils.constants import HTTP_201_CREATED , POST_UPLOADED_MESSAGE
import bson.json_util as json_util
from bson.objectid import ObjectId as Ob


def post():
    body = json.loads(request.data)
    
    url = body['url']
    caption = body['caption']
    userId = body['userId']
    
    posts = Posts(url , caption , userId)

    saved_posts = posts.save_posts()
    
    # json_version = json_util.dumps(saved_posts)
    
    return make_response({'message': POST_UPLOADED_MESSAGE} , HTTP_201_CREATED)


def add_postId():
    body = json.loads(request.data)
    
    userId = body['userId']
    
    postId = body['postId']
    
    post = Posts.add_posts(Ob(userId) , Ob(postId))
    print(post)
    
    return make_response({'message': "added postId in users posts!"} , HTTP_201_CREATED)
