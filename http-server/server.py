'''
server creation:
- create socket
- bind it to address:port 
- put into listening mode
'''
import socket
sock = socket.socket()
HOST = ''
PORT = 3000
sock.bind((HOST, PORT))
sock.listen()