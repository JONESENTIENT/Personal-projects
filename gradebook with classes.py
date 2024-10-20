gradebook = dict()

class student:
    def __init__(self, admin_no, name, marks):
        self.admin_no = admin_no
        self.name = name
        self.marks = marks

    def add_student(self):
        self.admin_no = admin_no
        self.name = name
        self.marks =marks

        gradebook[self.admin_no] = [self.name, self.marks]

    def delete_student(self):
        self.admin_no = admin_no
        gradebook.pop(self.admin_no)

    def edit_student(self):
        self.admin_no = input('Enter admission number: ')
        print('1-Name\n2-Maths\n3-English\n4-Science\n5-SST')
        self.choice = input('What field would you like to modify: ')

        if self.choice == '1':
            self.value = gradebook[self.admin_no]
            self.new_value = input('New value for name: ')
            self.value[0] = self.new_value
            gradebook[self.admin_no] = self.value

        elif self.choice == '2' or self.choice == '3' or self.choice == '4' or self.choice == '5':
            self.subs = ['Maths', 'English', 'Science', 'SST']
            self.value = gradebook[self.admin_no]
            self.new_value = input(f'New value for {self.subs[int(self.choice) - 2]}: ')
            self.value[1][int(self.choice) - 2] = self.new_value
            gradebook[self.admin_no] = self.value

        else:
            print('Invalid please!')

def print_gradebook():
    for key, value in gradebook.items():
        print(f'Admin n: {key} Name: {value[0]} Maths : {value[1][0]} English : {value[1][1]} Science : {value[1][2]} SST : {value[1][3]}')


while True:
    print('To add a student press a\nTo delete a student press d\nTo quit press q')
    entry = input('Enter your choice: ')
    if entry.upper() == 'A':
        marks = []
        admin_nos = list(gradebook.keys())
        admin_no = str(len(admin_nos) + 1)
        name = 'John Doe' #input('Enter name: ')
        subs =  ['Maths', 'English', 'Science', 'SST']

        choice = input('Enter marks now (Y/N): ')
        if choice.upper() == 'Y':
            for sub in subs:
                sub = input(f'Enter marks for {sub}: ')
                marks.append(sub)
        elif choice.upper() == 'N':
            marks = [0,0,0,0]
        else:
            print('Invalid input')

        person = student(admin_no, name, marks)
        person.add_student()
        print_gradebook()

    elif entry.upper() == 'D':
        admin_no = input('Enter admission number: ')
        value = gradebook[admin_no]
        person = student(admin_no, value[0], value[1])
        person.delete_student()
        print_gradebook()

    elif entry.upper() == 'Q':
        break

    else:
        print('Invalid input!')