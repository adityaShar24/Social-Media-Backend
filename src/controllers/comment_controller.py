from flask import request , json , make_response
from utils.constants import HTTP_201_CREATED , COMMENT_POSTED_MESSAGE , ADDED_COMMENTID_MESSAGE
from database.repositories.comment_repository import CommentsRepository
from database.repositories.user_repository import UserRepository
import bson.json_util as bson
from bson.objectid import ObjectId

def comment():
    body = json.loads(request.data)
    comment = body['comment']
    postId = body['postId']
    userId = body['userId']
    parent_commentId = body['parent_commentId'] if 'parent_commentId' in body else None
    
    saved_comments = CommentsRepository().create({'comment': comment , 'postId': ObjectId(postId) , 'userId': ObjectId(userId) , 'parent_commentId': parent_commentId})
    UserRepository().update_one({"_id": userId }, { "$push": { "comments": saved_comments } })
    
    json_saved_comments = bson.dumps(saved_comments)
    
    return make_response({'message': COMMENT_POSTED_MESSAGE, 'comment': json_saved_comments} , HTTP_201_CREATED)

