from flask_socketio import SocketIO , join_room , emit
from flask import request

socketio = SocketIO()

@socketio.on("connect")
def handle_connect():
    session_id = request.sid
    print(f"Client connected with session ID: {session_id}")
    
@socketio.on("join_room")
def handle_join_room(data):
    join_room(data["room"])
    print(f"Client joined room: {data['room']}")
    return { "message": "Joined room successfully." }