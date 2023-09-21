from flask import Blueprint
from controllers.user_controller import register , login , get_all_users
from flask_jwt_extended import jwt_required
from flask_caching import Cache
auth_bp = Blueprint('auth_bp' , __name__ )

cache = Cache(config={'CACHE_TYPE': 'simple'})

@auth_bp.post('/register')
def register_user_wrapper():
    return register()

@auth_bp.post('/login')
def login_user_wrapper():
    return login()

@auth_bp.get('/all-users')
@jwt_required()
@cache.cached(timeout=60)
def get_all_users_wrapper():
    return get_all_users()