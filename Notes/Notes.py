import os
import customtkinter as ctk
import json
from functools import partial

def verify():

    global right, welcome, vert, hor

    right = ctk.CTkFrame(app, width= 780, height=580, corner_radius=10)
    right.place(x=10,y=10)

    question = ctk.CTkLabel(right, width=600, height=500, text='Who is using Notes ?')
    question.place(x=0, y=530)

    welcome = ctk.CTkLabel(right, width=600, height=500, )
    welcome.place(x=60, y=50)
    
    vert = 10
    hor = 10
    try:
        with open('Users.json', 'r') as file:
            users = json.load(file)
            
            for key, value in users.items():
                try:
                    username = key
                    label = ctk.CTkButton(right, width=100, height=100,corner_radius=10, text=username, command=partial(start, value))
                    label.place(x=hor, y=vert)
                    if vert > 700:
                        hor += 110
                        vert = 10
                    else:
                        vert += 60
                    i += 1
                except:
                    continue
    except:
        label1 = ctk.CTkButton(right, width=100, height=100,corner_radius=10, text='New User', command=create_remove_user)
        label1.place(x=hor, y=vert)

        label2 = ctk.CTkButton(right, width=100, height=100,corner_radius=10, text='Guest', command=start)
        label2.place(x=hor, y=vert)

def create_remove_user(which):
    pass

def create_note():
    pass

def remove_note():
    pass

def open_note():
    pass

def save_note():
    pass

def start():    

    welcome.configure(text="""Let's make some Notes!\n\n\n\n\nNew - To create a new note.\n\n\n\n\nOpen - If you want to open a specific notes file (.note).\n\n\n\n\nRecents - To see all recent notes.""")
    right.configure(width=650)
    right.place(x=140, y=10)

    left = ctk.CTkFrame(app, width= 120, height=580, corner_radius=10)
    left.place(x=10,y=10)

    new = ctk.CTkButton(left, width=120, height=50, text='New',fg_color='transparent', hover_color=None, corner_radius=10)
    new.place(x=0, y=0)

    openn = ctk.CTkButton(left, width=120, height=50, text='Open', corner_radius=10,fg_color='transparent', hover_color=None)
    openn.place(x=0, y=60)

    recent = ctk.CTkButton(left, width=120, height=50, text='Recents', corner_radius=10,fg_color='transparent', hover_color=None)
    recent.place(x=0, y=120)

    settings = ctk.CTkButton(left, width=120, height=50, text='Setings', corner_radius=10,fg_color='transparent', hover_color=None)
    settings.place(x=0, y=470)

    quitt = ctk.CTkButton(left, width=120, height=50, text='Quit', corner_radius=10,fg_color='transparent', hover_color=None, command=quit)
    quitt.place(x=0, y=530)



app = ctk.CTk()
app.geometry('800x600')
app.maxsize(800,600)
app.minsize(800,600)
app.title('Notes')

verify()
start()

app.mainloop()
