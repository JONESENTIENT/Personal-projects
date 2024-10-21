import pygame
import sys
import os
import customtkinter as ctk

def play_audio(file_path):
    pygame.mixer.init(frequency=44100, size=-16, channels=2)
    
    try:
        pygame.mixer.music.load(file_path)
    except pygame.error as e:
        print(f"Error loading file: {e}")
        return

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def find_audio_files(start_directory):
    audio_extensions = ('.mp3', '.m4a', '.wav')
    audio_files = {}
    global num
    num = 0
    for dirpath, _, filenames in os.walk(start_directory):
        for filename in filenames:
            if filename.lower().endswith(audio_extensions):
                file_path = os.path.join(dirpath, filename)
                audio_files[file_path] = filename
                num += 1

    return audio_files

app = ctk.CTk()
app.geometry('800x600')
app.title('Audio Player')
if __name__ == "__main__":
    start_dir = r'C:\Users\LENOVO'
    audio_files_dict = find_audio_files(start_dir)

    if not audio_files_dict:
        print("No audio files found.")
        sys.exit()

    print(f"Found audio files:{num}")
    
    slides = []
    for value in audio_files_dict.values():
        slides.append(value)
        
    #code to play song from dictionary
    
    pygame.quit()
    sys.exit()

app.mainloop()