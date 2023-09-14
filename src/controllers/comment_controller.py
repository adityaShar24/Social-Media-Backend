from flask import request , json , make_response
from utils.constants import HTTP_201_CREATED , COMMENT_POSTED_MESSAGE , ADDED_COMMENTID_MESSAGE
from models.comment_model import Comment
import bson.json_util as bson


def comment():
    body = json.loads(request.data)
    comment = body['comment']
    postId = body['postId']
    userId = body['userId']
    parent_commentId = body['parent_commentId'] if 'parent_commentId' in body else None
    
    user_comment = Comment(comment , postId , userId , parent_commentId)
    
    saved_comments = user_comment.save_comments()
    
    json_saved_comments = bson.dumps(saved_comments)
    
    return make_response({'message': COMMENT_POSTED_MESSAGE, 'comment': json_saved_comments} , HTTP_201_CREATED)


def add_commentId():
    body = json.loads(request.data)
    
    userId = body['userId']
    commentId = body['commentId']
    
    Comment.add_commentId(userId , commentId)
    
    return make_response({'message' : ADDED_COMMENTID_MESSAGE } , HTTP_201_CREATED)