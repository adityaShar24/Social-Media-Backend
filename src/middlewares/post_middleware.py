from flask import request , json , make_response
from utils.constants import HTTP_400_BAD_REQUEST , ADD_POST_ENDPOINT

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