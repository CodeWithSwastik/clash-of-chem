import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)

users = {}
rooms = {}

@sio.event
async def connect(sid, environ, auth):
    if auth is None:
        return False

    print(sid, "connected", auth)
    sio.enter_room(sid, auth['room'])
    rooms[auth['room']] = rooms.get(auth['room'], {"players": []})
    rooms[auth['room']]["players"].append(auth['username'])
    users[sid] = auth
    await sio.emit('room_details', {'data': rooms[auth['room']]["players"]}, room=auth['room'])
    await sio.emit('user_join', {'data': auth['username']}, room=auth['room'])

@sio.event
async def disconnect(sid):
    print(sid, "disconnected")
    room = users[sid]['room']
    username = users[sid]['username']
    sio.leave_room(sid, room)
    rooms[room]["players"] = [x for x in rooms[room]["players"] if x != username] 
    await sio.emit('user_leave', {'data': {"players": rooms[room]["players"]}}, room=room)