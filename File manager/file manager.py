import customtkinter as ctk
import os

root = ctk.CTk()
root.geometry('800x600')
root.title('Study Folder')

study_folder = r'C:\Users'

folder_list = [f for f in os.listdir(study_folder) if not os.path.isfile(os.path.join(study_folder, f))]
file_list = [f for f in os.listdir(study_folder) if os.path.isfile(os.path.join(study_folder, f))]

print(folder_list, file_list)

#root.mainloop()