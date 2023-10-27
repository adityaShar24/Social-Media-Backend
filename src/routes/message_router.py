from flask import Blueprint
from controllers.message_controller import send_message

message_bp = Blueprint('message_bp', __name__)

@message_bp.post('/send-message')
def send_message_wrapper():
    return send_message()

