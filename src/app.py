from flask import Flask
from routes.user_router import auth_bp , cache
from routes.request_router import request_bp
from routes.post_router import post_bp
from routes.comment_router import comment_bp
from routes.rooms_router import rooms_bp
from routes.message_router import message_bp
from flask_jwt_extended import JWTManager
from middlewares.user_middleware import register_user_middleware , login_user_middleware
from middlewares.request_middleware import make_request_middleware , remove_friend_request_middleware , accept_request_middleware , reject_request_middleware 
from middlewares.post_middleware import post_middleware ,save_post_middleware
from middlewares.comment_middleware import comment_middleware , add_commentId_middleware
from middlewares.rooms_middleware import create_room_middleware , add_member_middleware
from middlewares.message_middleware import send_message_middleware
from routes.events import socketio

app = Flask(__name__)

JWTManager(app)

cache.init_app(app)
socketio.init_app(app)

app.config['SECRET_KEY'] = "my_secret_key_part_4"

app.before_request(register_user_middleware)
app.before_request(login_user_middleware)

app.before_request(make_request_middleware)
app.before_request(accept_request_middleware)
app.before_request(reject_request_middleware)
app.before_request(remove_friend_request_middleware)

app.before_request(post_middleware)
app.before_request(save_post_middleware)

app.before_request(comment_middleware)
app.before_request(add_commentId_middleware)

app.before_request(create_room_middleware)
app.before_request(add_member_middleware)

app.before_request(send_message_middleware)

app.register_blueprint(auth_bp)
app.register_blueprint(request_bp)
app.register_blueprint(post_bp) 
app.register_blueprint(comment_bp)
app.register_blueprint(rooms_bp)
app.register_blueprint(message_bp)

if __name__ == '__main__':
    socketio.run(app , host='0.0.0.0' , debug = True)
    