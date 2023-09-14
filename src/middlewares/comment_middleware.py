from flask import request, json , make_response
from utils.constants import COMMENT_REQUIRED , COMMENT_ENDPOINT , HTTP_400_BAD_REQUEST , POSTID_MISSING_ERROR , USER_ID_MISSING_ERROR , PARENT_COMMENTID_MISSING_ERROR

def comment_middleware(request):
    if request.endpoint == COMMENT_ENDPOINT:
        body = json.loads(request.data) 
        comment = body['comment']
        postId = body['postId']
        userId = body['userId']
        parent_commentId = body['parent_commentId'] if 'parent_commentId' in body else None
        
        if not comment:
            return make_response({'message' : COMMENT_REQUIRED} , HTTP_400_BAD_REQUEST)
        
        if not postId:
            return make_response({'message': POSTID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not userId: 
            return make_response({'message' : USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
        
        if not parent_commentId:
            return make_response({'message' : PARENT_COMMENTID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
