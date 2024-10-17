import socket

HEADER = 64
PORT = 5050 #pick a port to run on
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname()) #automatically get ip adress
DISCONNECT_MESSAGE = 'Conn Lost'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# to connect to server
client.connect(ADDR)

def send():
    receipient = input('Enter receiver: ')
    receipt = receipient.encode(FORMAT)
    receipt_length = len(receipt)
    receipt_length = str(receipt_length).encode(FORMAT)
    receipt_length += b'' * (HEADER - len(receipt_length))

    msg = input('Enter message: ')
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b'' * (HEADER - len(send_length))

    client.send(receipt_length)
    client.send(receipt)
    
    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))

send()