from flask import Blueprint
from controllers.post_controller import post

post_bp = Blueprint('post_bp' , __name__)

@post_bp.post('/post')
def post_wrapper():
    return post()
