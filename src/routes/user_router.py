from flask import Blueprint
from controllers.user_controller import register , login , make_request , remove_request
auth_bp = Blueprint('auth_bp' , __name__ )


@auth_bp.post('/register')
def register_user_wrapper():
    return register()

@auth_bp.post('/login')
def login_user_wrapper():
    return login()

@auth_bp.post('/make-request')
def make_request_wrapper():
    return make_request()

@auth_bp.delete('/remove_request')
def remove_request_wrapper():
    return remove_request()