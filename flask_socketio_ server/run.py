from Server import create_app, socketio
app = create_app()

socketio.run(app, host='192.168.0.22', port=5000)