from flask import Blueprint
from controllers.post_controller import post , add_postId

post_bp = Blueprint('post_bp' , __name__)

@post_bp.post('/post')
def post_wrapper():
    return post()

@post_bp.post('/add-postId')
def add_postId_wrapper():
    return add_postId()