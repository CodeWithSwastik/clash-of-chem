import socketio
from .models import User, Room
from typing import Dict

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = socketio.ASGIApp(sio)

users: Dict[str, User] = {}
rooms: Dict[str, Room] = {}


@sio.event
async def connect(sid, environ, auth):
    if auth is None:
        return False

    print(sid, "connected", auth)
    user = User(sid, auth["username"], auth["room"])
    users[sid] = user

    sio.enter_room(sid, user.room_id)

    if user.room_id in rooms:
        rooms[user.room_id].add_player(user)
    else:
        rooms[user.room_id] = Room.create(user)

    room = rooms[user.room_id]
    await sio.emit("room_details", {"data": room.player_names}, room=user.sid)
    await sio.emit("user_join", {"data": room.player_names}, room=room.id)


@sio.event
async def disconnect(sid):
    print(sid, "disconnected")
    user = users[sid]
    room = rooms[user.room_id]
    sio.leave_room(sid, room.id)
    room.remove_player(user)

    await sio.emit("user_leave", {"data": room.player_names}, room=room.id)
