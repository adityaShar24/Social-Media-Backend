from flask import Flask
from routes.user_router import auth_bp , cache
from routes.request_router import request_bp
from routes.post_router import post_bp
from flask_jwt_extended import JWTManager
from middlewares.user_middleware import register_user_middleware , login_user_middleware
from middlewares.request_middleware import make_request_middleware , remove_friend_request_middleware , response_request_middleware
from middlewares.post_middleware import post_middleware

app = Flask(__name__)

JWTManager(app)

cache.init_app(app)

app.config['SECRET_KEY'] = "my_secret_key"
app.config['CACHE_TYPE'] = 'simple'

app.before_request(register_user_middleware)
app.before_request(login_user_middleware)

app.before_request(make_request_middleware)
app.before_request(response_request_middleware)
app.before_request(remove_friend_request_middleware)

app.before_request(post_middleware)

app.register_blueprint(auth_bp)
app.register_blueprint(request_bp)
app.register_blueprint(post_bp) 


if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)