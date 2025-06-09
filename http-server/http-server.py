import socket

with socket.socket() as s:
    HOST = ''
    PORT = 3000
    s.bind((HOST, PORT))
    print(f"server has binded to {HOST}: {PORT}")
