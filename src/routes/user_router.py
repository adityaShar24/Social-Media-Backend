from flask import Blueprint
from controllers.user_controller import register

auth_bp = Blueprint(__name__ , 'auth_bp')


@auth_bp.post('/register')
def register_user_wrapper():
    return register()

