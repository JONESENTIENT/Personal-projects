import customtkinter as ctk
import sys_info as si

class widget:
    def __init__(self,layer, width, height, c_rad, text, command, x, y):
        self.layer = layer
        self.width = width
        self.height = height
        self.c_rad = c_rad
        self.text = text 
        self.command = command
        self.x, self.y = x,y

    def create(self):
        button = ctk.CTkButton(self.layer, self.width, self.height, self.c_rad, self.text, self.command)
        button.place(self.x, self.y)


    def config_text(self, text):
        self.text = text

class label(widget):
    def __init__(self,layer, width, height, c_rad, text, x, y):
        super.__init__(self,layer, width, height, c_rad, text, x, y)

class frame:
    def __init__(self, layer, width, height, c_rad, x, y):
        super.__init__(self, layer, width, height, c_rad, x, y)

def home():
    si.run()

def test():
    pass

def diag():
    pass

root = ctk.CTk()
root.geometry('1200x720')
root.title('Diagnostics')

homes = None
tests = None
diagnostics = None
buttons = [('HOME',home,homes), ('TESTS',test,tests), ('DIAGNOSTICS', diag,diagnostics)]
i = 0
y = 20
for buton,func,button in buttons:
    button = widget(root, 100, 50, 5, buton, func, 20, y)
    button.create()
    y += 60


root.mainloop()
        