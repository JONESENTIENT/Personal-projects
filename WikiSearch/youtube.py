import requests
from bs4 import BeautifulSoup
import customtkinter as ctk

global subject

def stop():
    quit()

def save():
    text = result_pane.get('1.0', 'end')
    filename = get_info() + '.docx'
    with open(filename, 'w') as file:
        file.write(text)


def get_info():
    subject = subject_entry.get().strip()
    if len(subject) == 0:
        subject = 'Empty'
        result_pane.insert('end', "Enter search please!!!\n")
        return subject

    else:
        subject = subject_entry.get().strip()
        # subject to append onto wikipedia website
        url = f"https://en.wikipedia.org/wiki/{subject}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.find('h1').get_text()
            first_paragraph = soup.find('p').get_text()

            sections = soup.find_all(['h2', 'p'])
            result_pane.configure(state='normal')
            result_pane.delete('1.0', 'end')
            result_pane.insert('end', f"Title: {title}\n\nFirst Paragraph: {first_paragraph}\n\n")


            for section in sections:
                if section.name == 'h2':
                    result_pane.insert('end', f"\n{section.get_text(strip=True)}\n")
                elif section.name == 'p':
                    result_pane.insert('end', f"{section.get_text(strip=True)}\n")

            result_pane.configure(state='disabled')
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            result_pane.insert('end', "Connect to the internet !!\n")

        return subject
    


app = ctk.CTk()
app.geometry('800x600')
app.title('Portable Wiki')

subject_entry = ctk.CTkEntry(app, width=600, height=50)
subject_entry.place(x=100, y=10)

search_button = ctk.CTkButton(app, width=80, height=50, text='Search', command=get_info)
search_button.place(x=710, y=10)

result_pane = ctk.CTkTextbox(app, width=780, height=520)
result_pane.place(x=10, y=70)

save_button = ctk.CTkButton(app, width=80, height=20, text='Save', command=save)
save_button.place(x=10, y=10)

close_button = ctk.CTkButton(app, width=80, height=20, text='Close', command=stop)
close_button.place(x=10, y=40)

app.mainloop()
