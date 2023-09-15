from flask import request, json , make_response
from utils.constants import COMMENT_REQUIRED , COMMENT_ENDPOINT , HTTP_400_BAD_REQUEST , POSTID_MISSING_ERROR , USER_ID_MISSING_ERROR , COMMENTID_MISSING_ERROR , ADD_COMMENTID_ENDPOINT


def comment_middleware():
    if request.endpoint == COMMENT_ENDPOINT:
        body = json.loads(request.data) 
        comment = body['comment']
        postId = body['postId']
        userId = body['userId']
        
        if not comment:
            return make_response({'message' : COMMENT_REQUIRED} , HTTP_400_BAD_REQUEST)
        
        if not postId:
            return make_response({'message': POSTID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not userId: 
            return make_response({'message' : USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
def add_commentId_middleware():
    if request.endpoint == ADD_COMMENTID_ENDPOINT:
        body = json.loads(request.data)
        
        postId = body['postId']
        commentId = body['commentId']
        
        if not postId: 
            return make_response({'message' : POSTID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not commentId:
            return make_response({'message' :  COMMENTID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        