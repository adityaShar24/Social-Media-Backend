from flask import Blueprint
from controllers.comment_controller import comment


comment_bp = Blueprint('comment_bp' , __name__)

@comment_bp.post('/comment')
def comment_wrapper():
    return comment()
