from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_caching import Cache
from controllers.rooms_controller import create_room , add_member , get_all_rooms

rooms_bp = Blueprint('rooms_bp' , __name__ )

cache = Cache(config={'CACHE_TYPE': 'simple'})

@rooms_bp.post('/create-room')
@jwt_required()
def create_room_wrapper():
    return create_room()



