import customtkinter as ctk
import datetime
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

def send(msg):

    message = msg.encode(FORMAT)
    msg_length = len(message)
    msg_length = str(msg_length).encode(FORMAT)
    msg_length += b'' * (HEADER - len(msg_length))

    client.send(msg_length)
    client.send(message)

def send_message():
    message_part = message_box.get('1.0', 'end-1c')
    receiver = receiver_box.get()
    sender = sender_box.get()
    message = receiver+'@'+sender+'@'+message_part
    send(message)

def message():
    receiver_frame = ctk.CTkFrame(root, width=780, height=50, corner_radius=10)
    receiver_frame.place(x=10, y=10)
    label = ctk.CTkLabel(root, width=40, height=30, text = 'Receiver:')
    label.place(x=20, y=20)

    global receiver_box
    receiver_box = ctk.CTkEntry(root, width=700, height=30, corner_radius=10,placeholder_text='To?')
    receiver_box.place(x=80, y=20) 

    global message_box
    message_frame = ctk.CTkFrame(root, width=780, height=520, corner_radius=10)
    message_frame.place(x=10, y=70)

    message_box = ctk.CTkTextbox(message_frame, width=760, height=430, corner_radius=10)
    message_box.place(x=10, y=80)

    global sender_box
    sender_box = ctk.CTkEntry(message_frame, width=650, height=40, corner_radius=10, placeholder_text='From?')
    sender_box.place(x=10, y=10)

    send_button = ctk.CTkButton(message_frame, width=100, height=40, text='Send', corner_radius=10, command=send_message)
    send_button.place(x=670, y=10)
    
root = ctk.CTk()
root.geometry('800x600')
root.title('C-S PING')

message()

root.mainloop()