def newuser():
    username = input('Enter username : ')

    pwd1 = input('Enter password : ')
    pwd2 = input('Enter password again : ')

    while pwd1 != pwd2:
        pwd1 = input('Enter password : ')
        pwd2 = input('Enter password again : ')

    print (f'Hello {username}, your password is {pwd1}, please note it as it wont be visible again!')

    with open('Users.file', 'a') as file:
        file.write(username + ' ' + pwd1 + '\n')
    
    userfile = username  + '.file'
    with open(userfile, 'w') as file:
        file.close()

    openuser()

def openuser():
    users = []
    usernames = []
    passwords = []
    with open('Users.file', 'r') as file:
        users = file.readlines()
        for user in users:
            user.strip()
            userswithpasswords = user.split(' ')
            usernames.append(userswithpasswords[0])
            passwords.append(userswithpasswords[1])

    index = 0
    indexes = []

    print('Enter the number corresponding to your username;')
    for username in usernames:
        print(f'{index} : {username}\n')
        indexes.append(index)
        index += 1
    choice = int(input('You are user number : '))

    for index in indexes:
        if choice == index:
            with open('Users.file', 'r') as file:
                users = [user.strip() for user in file.readlines()]
                usernamewithpassword = users[index]
                wordlist = usernamewithpassword.split(' ')
                username = wordlist[0] + '.file'
                password = wordlist[1]

            entry = input('Enter password : ')
            if entry == password:
                with open(username, 'r') as file:
                    pwds = [pwd.strip() for pwd in file.readlines()]
                    for pwd in pwds:
                        print(pwd + '\n')

                choice = input('For new password press N, to quit press Q : ')
                if choice == 'N' or choice == 'n':
                    pwdname = input('What is this password for : ')
                    pwdnew = input('What is the password : ')

                    with open(username + '.file', 'w') as file:
                        file.write(pwdname + pwdnew + '\n')
                        pwds = [pwd.strip() for pwd in file.readlines()]
                        for pwd in pwds:
                            print(pwd + '\n')
                
                else:
                    quit()

            else:
                print('Wrong password!!')
            break
        else:
            print('User not found')


def start():
    choice = input('New user? Enter Y/N :')
    if choice == 'Y' or choice == 'y':
        newuser()

    elif choice == 'N' or choice == 'n':
        openuser()

    else:
        print('Invalid input')

while True:
    start()

