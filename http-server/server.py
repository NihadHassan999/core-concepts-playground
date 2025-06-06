'''
echo server creation:
- create socket
- bind it to address:port 
- put into listening mode
'''
import socket

server_sock = socket.socket()
HOST = ''
PORT = 3000
server_sock.bind((HOST, PORT))
print(f"server has binded to {HOST}:{PORT}")
server_sock.listen()

'''
echo server operation:
- create infinite loop to handle multiple clients over time
- accept connections and handle them
- echo back
'''
while True:
    print("Server entered infinite loop") 
    conn, address = server_sock.accept()
    with conn:
        print(f"Connected by : {address}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
