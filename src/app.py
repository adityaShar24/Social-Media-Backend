from flask import Flask
from routes.user_router import auth_bp , cache
from routes.request_router import request_bp
from routes.post_router import post_bp
from routes.comment_router import comment_bp
from flask_jwt_extended import JWTManager
from middlewares.user_middleware import register_user_middleware , login_user_middleware
from middlewares.request_middleware import make_request_middleware , remove_friend_request_middleware , accept_request_middleware , reject_request_middleware 
from middlewares.post_middleware import post_middleware , add_postId_middleware
from middlewares.comment_middleware import comment_middleware , add_commentId_middleware

app = Flask(__name__)

JWTManager(app)

cache.init_app(app)

app.config['SECRET_KEY'] = "my_secret_key"

app.before_request(register_user_middleware)
app.before_request(login_user_middleware)

app.before_request(make_request_middleware)
app.before_request(accept_request_middleware)
app.before_request(reject_request_middleware)
app.before_request(remove_friend_request_middleware)

app.before_request(post_middleware)
app.before_request(add_postId_middleware)

app.before_request(comment_middleware)
app.before_request(add_commentId_middleware)

app.register_blueprint(auth_bp)
app.register_blueprint(request_bp)
app.register_blueprint(post_bp) 
app.register_blueprint(comment_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)
    