import tkinter as tk
import customtkinter as ctk
import os


run=True

def appenduserlist():
    #basedir= os.path.expanduser("~")
    #filename="Users.txt"
    #userfolderpath = os.path.join(basedir,"Desktop", "LITE", "User folder")
    #os.chdir(userfolderpath)
    with open('Users.txt', "a") as file:
       file.write("\n" + newusername)


#INSTANCE FRAMES

#newuser
def newuser():
    newuserframe=ctk.CTkFrame(app,width=600, height=400)
    newuserframe.place(x=0,y=0)

    username=ctk.CTkEntry(newuserframe, width=100, height=40)
    username.place(x=250, y=50)
    global newusername
    newusername = username.get()
    signinbutton=ctk.CTkButton(newuserframe, text="Sign In", width=50, height=40, command=appenduserlist)
    signinbutton.place(x=275, y=100)
    
    

#userlist instance
def userlistdisplay():
    userframe=ctk.CTkFrame(app, width=600, height=400)
    userframe.place(x=0, y=0)
    global users
    users=[]
    userfolderpath="User folder"
    if os.path.getsize(userfolderpath)==0:
        newuserbutton=ctk.CTkButton(userframe, text="New User", command=newuser ,width=100, height=40)
        newuserbutton.place(x=250, y=10)
    else:
        with open(userfolderpath, "r") as file:
            for line in file:
                users.append(line.strip())
            for user in users:
                userbutton=ctkCTkButton(userframe, text= user, command=lambda u=user: userselect(u))
                userbutton.pack(pady=10)
                global u;
                global selecteduser
                selecteduser=tk.StringVar()
                selecteduser.set(user)
                print(user)
                
#Start frame
def start():
    mainframe=ctk.CTkFrame(app, width=600, height=400)
    mainframe.place(x=0, y=0)
    userlistdisplay()

#user folder check
userfolderpath="User folder"
if os.path.exists(userfolderpath):
    print("Folder wxists")
else:
    userlist=os.path.join(userfolderpath, "Users.txt")
    os.makedirs(userfolderpath, exist_ok=True)

#passwords folder check
passwordfolderpath="Password folder"
if os.path.exists(passwordfolderpath):
    print("Folder exists")
else:
    passwordlist=os.path.join(passwordfolderpath, "Passwords.txt")
    os.makedirs(passwordfolderpath, exist_ok=True)
    

#window class
while run:
    app=ctk.CTk()
    app.geometry("600x400")
    app.title("Lite")
    app.resizable(False, False)
    app.maxsize(600,400)
    start()
    userlistdisplay()
    app.mainloop()
    app.destroy()
