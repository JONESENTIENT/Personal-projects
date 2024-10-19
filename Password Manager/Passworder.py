import random
import customtkinter as ctk

def generate():
    letters = r'abcdefghijklmopqrstuvwxyz 0123456789#.,@\n/?-_'

    word = ''
    for j in range(10):
        number = random.randint(0,45)
        letter = letters[number]
        word += letter

    label.configure(text=word)

root = ctk.CTk()
root.geometry('500x130')
root.title('Password generator')
default = 'Click randomize to generate strong password :)'

frame = ctk.CTkFrame(root, width=340, height=45, border_width=5)
frame.place(x=20,y=10)

label = ctk.CTkLabel(frame, width=340, height=45, text=default)
label.place(x=0,y=0)

button = ctk.CTkButton(root, width=100, height=45, text='Generate', command=generate)
button.place(x=380,y=10)

choice1 = ctk.CTkRadioButton(root, width=125, height=50, text='Include spaces?')
choice1.place(x=200, y=70)

choice2 = ctk.CTkRadioButton(root, width=125, height=50, text='Include alphanumerics?')
choice2.place(x=350, y=70)

root.mainloop()
