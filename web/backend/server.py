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
    user = users[sid]
    print(sid, user.username, "disconnected")

    room = rooms[user.room_id]
    sio.leave_room(sid, room.id)
    room.remove_player(user)
    if room.players:
        await sio.emit("user_leave", {"data": {"players":room.players_info, "owner":room.owner.username}}, room=room.id)
    else:
        del rooms[room.id], room


@sio.event
async def start_clash(sid, data):
    room = rooms[data["room"]]
    if room.owner.sid != sid:
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
        await sio.emit("clash_over", {"data": clash.winner}, room=clash.id)
        del clashes[clash.id], clash


@sio.event
async def clash_answer(sid, data):
    clash = clashes[data["clash"]]
    user = users[sid]
    if data["answer"] == clash.game.current_challenge.correct_reagent:
        clash.game.clear_challenge(user.username)
        await sio.emit("clash_details", {"data": clash.clash_info}, room=clash.id)
        return True
    else:
        return False

@sio.event
async def clash_strategy_update(sid, data):
    clash = clashes[data["clash"]]
    user = users[sid]
    if clash.game.current_challenge.turn != user.username:
        return False
    else:
        clash.game.strategy_update(data["reagent"])
        await sio.emit("new_challenge", {"data": clash.game.current_challenge.challenge_data}, room=clash.id)

        if clash.game.current_challenge.winner:
            await sio.emit("clash_details", {"data": clash.clash_info}, room=clash.id)

        
