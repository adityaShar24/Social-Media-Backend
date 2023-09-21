from flask import request , json , make_response
from models.abstract_model import PostsRepository, UserRepository, AbstractRepository
from utils.constants import HTTP_201_CREATED , POST_UPLOADED_MESSAGE
import bson.json_util as json_util
from bson.objectid import ObjectId as Ob


def post():
    body = json.loads(request.data)
    
    url = body['url']
    caption = body['caption']
    userId = body['userId']
    
    postId = PostsRepository().create({'url':url , 'caption':caption , 'userId':Ob(userId)})
    UserRepository().updateOne({"_id": Ob(userId) }, { "$push": { "posts": Ob(postId) } })
    
    return make_response({'message': POST_UPLOADED_MESSAGE, "postId":json_util.dumps(postId) } , HTTP_201_CREATED)
