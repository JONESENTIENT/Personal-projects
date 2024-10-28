import random
import customtkinter as ctk

def generate():
    letters = r'abcdefghijklmopqrstuvwxyz 0123456789#.,@\n/?-_'

    word = ''
    num = choice3.get()
    space = choice1.cget()
    alpha = choice2.cget()
    print(space, alpha)
    if num >= 4 and num <= 10:
        for j in range(num):
            number = random.randint(0,45)
            letter = letters[number]
            if space == 0:
                if letter in r' ':
                    continue
            elif alpha == 0:
                if letter in r'#.,@\n/?-_':
                    continue
            else:
                word += letter

        label.configure(text=word)
    elif num < 4 or num > 10:
        label.configure(text = 'Too few/many characters!')

    else:
        label.configure(text = 'Invalid password length!')

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
choice1.place(x=180, y=70)

choice2 = ctk.CTkRadioButton(root, width=125, height=50, text='Include alphanumerics?')
choice2.place(x=330, y=70)

choice3 = ctk.CTkEntry(root, width=50, height=50)
choice3.place(x=10, y=70)

label2 = ctk.CTkLabel(root, width=90, height=50, text='Characters (4-10)')
label2.place(x=60,y=70)

root.mainloop()
