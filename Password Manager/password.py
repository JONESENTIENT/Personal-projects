def save_user(username, password):
    users[username] = password
    

def new_user():
    username = input('Choose a username: ')
    password = input('Choose a password: ')
    while True:
        password_repeat = input('Repeat the password: ')
        if password_repeat == password:
            break
        print('Passwords dont match !!')
    save_user(username, password)
    open_user(username, password)
def open_user(username, password):
    pass

try:
    with open('users.json', 'x') as file:
        file.close()
except:
    pass

while True:
    print('New user? Y/N: ')
    print('Press Q to quit: ')

    choice = input('Enter choice: ')
    if choice.upper() == 'Y':
        new_user()
    elif choice.upper() == 'N':
        open_user()
    elif choice.upper() == 'Q':
        quit()
    else:
        print('Invalid Input!!')