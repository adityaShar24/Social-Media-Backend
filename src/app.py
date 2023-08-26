from flask import Flask
from routes.user_router import auth_bp
from flask_jwt_extended import JWTManager
from middlewares.user_middleware import register_user_middleware , login_user_middleware

app = Flask(__name__)

JWTManager(app)

app.config['SECRET_KEY'] = "my_secret_key"

app.before_request(register_user_middleware)
app.before_request(login_user_middleware)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True)