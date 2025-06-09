"""
sample echo client
- create socket instance
- connect()
- send message
- echo back
"""
import socket

with socket.socket() as client_socket:
    HOST = 'localhost'
    PORT = 3000
    client_socket.connect((HOST, PORT))
    message = "Hello World"
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print('Recieved', repr(data))