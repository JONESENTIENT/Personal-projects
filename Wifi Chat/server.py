import socket
import threading #sreate multiple threads in the same program ie run multiple instances at once

HEADER = 64
PORT = 5050 #pick a port to run on
SERVER = '10.10.129.195' #pick an ip adress for server, local or public in this case ill use mine
SERVER = socket.gethostbyname(socket.gethostname()) #automatically get ip adress
ADDR = (SERVER,PORT) #this tuple binds the socket to the address
FORMAT = 'utf-8'
global DISCONNECT_MESSAGE
DISCONNECT_MESSAGE = 'Conn Lost'

# create socket that is a data passage
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'New Connection: {addr} connected')
    connected = True
    while connected:

            msg_length = conn.recv(HEADER).decode(FORMAT)
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            message = []
            message = msg.split('@')

            print(f'{addr}: {message[1]} sent {message[2]} to {message[0]}')           

    conn.close()

def start():
    server.listen()
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active Connections: {threading.active_count() - 1}')

print('Server is starting.....')

start()
    