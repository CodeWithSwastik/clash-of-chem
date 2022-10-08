import asyncio
import socketio
from .models import User, Room, Clash
from typing import Dict

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = socketio.ASGIApp(sio)

users: Dict[str, User] = {}
rooms: Dict[str, Room] = {}
clashes: Dict[str, Clash] = {}


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
    await sio.emit("room_details", {"data": room.room_info}, room=user.sid)
    await sio.emit("user_join", {"data": room.players_info}, room=room.id)


@sio.event
async def disconnect(sid):
    print(sid, "disconnected")
    user = users[sid]
    room = rooms[user.room_id]
    sio.leave_room(sid, room.id)
    room.remove_player(user)
    if room.players:
        await sio.emit("user_leave", {"data": room.players_info}, room=room.id)
    else:
        del rooms[room.id], room


@sio.event
async def start_clash(sid, data):
    room = rooms[data["room"]]
    print("1")
    if room.owner.sid != sid:
        print("2")
        return False
    else:
        clash = room.create_clash()
        clashes[clash.id] = clash
        del room, rooms[clash.id]

        print("Clash Started")
        await sio.emit("clash_started", room=clash.id)
        await asyncio.sleep(2)
        await sio.emit("clash_details", {"data": clash.clash_info}, room=clash.id)
        for challenge in clash.game:
            print(challenge)
            await sio.emit("new_challenge", {"data": challenge}, room=clash.id)
            await asyncio.sleep(challenge["time"])

        print("Clash over")


@sio.event
async def clash_answer(sid, data):
    clash = clashes[data["clash"]]
    user = users[sid]
    if data["answer"] == clash.game.current_challenge.correct_reagent:
        clash.game.clear_challenge(user.username)
        await sio.emit("clash_details", {"data": clash.clash_info}, room=clash.id)
