from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Lista para almacenar los mensajes
mensajes = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('enviar mensaje')
def handle_message(data):
    mensaje = {'usuario': data['usuario'], 'mensaje': data['mensaje']}
    mensajes.append(mensaje)
    emit('nuevo mensaje', mensaje, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
