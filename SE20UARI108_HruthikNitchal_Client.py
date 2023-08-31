import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('send_message')
def on_message(data):
    print(f'Received message: {data["message"]}')
    sio.emit('response', {'response': 'Message received successfully!'})
    sio.disconnect()

if _name_ == '_main_':
    message_to_send = input("Enter your message: ")

    sio.connect('http://localhost:8888')
    sio.emit('send_message', {'message': message_to_send})
    sio.wait()