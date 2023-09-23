from flask import request , json , make_response
from utils.constants import HTTP_400_BAD_REQUEST , ADD_POST_ENDPOINT , USER_ID_MISSING_ERROR , POSTID_MISSING_ERROR , SAVE_POST_ENDPOINT

def post_middleware():
    if request.endpoint == ADD_POST_ENDPOINT:
        body = json.loads(request.data)
            
        url = body['url']
        caption = body['caption']
        userId = body['userId']
            
        if not url:
            return make_response({'message':'Post url should not be empty'} , HTTP_400_BAD_REQUEST)
            
        if not caption:
            return make_response({'message':'Post caption should not be empty'} , HTTP_400_BAD_REQUEST)
            
        if not userId:
            return make_response({'message':"userId cannot be empty"} , HTTP_400_BAD_REQUEST)
            

def save_post_middleware():
    if request.endpoint == SAVE_POST_ENDPOINT:
        body = json.loads(request.data)
        
        userId = body['userId']
        
        postId = body['postId']
        
        if not userId:
            return make_response({'message': USER_ID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)
            
        if not postId:
            return make_response({'message': POSTID_MISSING_ERROR} , HTTP_400_BAD_REQUEST)