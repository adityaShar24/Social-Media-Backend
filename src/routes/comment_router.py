from flask import Blueprint
from controllers.comment_controller import comment , add_commentId


comment_bp = Blueprint('comment_bp' , __name__)

@comment_bp.post('/comment')
def comment_wrapper():
    return comment()

@comment_bp.post('/add-commentId')
def add_commmenId_wrapper():
    return add_commentId()