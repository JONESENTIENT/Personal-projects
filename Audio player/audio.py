import pygame
import sys
import os
import customtkinter as ctk
from functools import partial
import threading

vert = 20
i = 0

def play_audio(path):
    # get position of song
    pygame.mixer.init(frequency=44100, size=-16, channels=2)
    
    try:
        pygame.mixer.music.load(path)
    except pygame.error as e:
        print(f"Error loading file: {e}")
        return

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def find_audio_files(start_directory):
    audio_extensions = ('.mp3', '.m4a', '.wav')
    keys,values = [],[]
    global num
    num = 0
    for dirpath, _, filenames in os.walk(start_directory):
        for filename in filenames:
            if filename.lower().endswith(audio_extensions):
                file_path = os.path.join(dirpath, filename)
                keys.append(file_path)
                values.append(filename)
                num += 1

    return [keys, values]

def start(key):
    thread = threading.Thread(target = play_audio(key))
    thread.start()
    thread.join()

app = ctk.CTk()
app.geometry('800x600')
app.title('Audio Player')


start_dir = r'C:\Users\LENOVO\Music'
songs = find_audio_files(start_dir)

if not songs:
    sys.exit()

# CANVAS
canvas = ctk.CTkCanvas(app)
scrollbar = ctk.CTkScrollbar(app, orientation='vertical', command=canvas.yview)
scrollable_frame = ctk.CTkFrame(canvas, width=760)

#configure scrollbar
scrollable_frame.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox(all)))
canvas.create_window((0,0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)
    
#code to play song from dictionary
for j in range(num):
    try:
        key = songs[0][i]
        value = songs[1][i]
        label = ctk.CTkButton(scrollable_frame, width=760, height=50,corner_radius=5, text=value, command=partial(start, key), anchor='nw')
        label.place(x=20, y=vert)
        vert += 60
        i += 1
    except:
        continue

#layout
canvas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

app.mainloop()