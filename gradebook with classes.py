import os

your_name = 'Mawande JohnPaul'
your_reg_number = '24/U/0678'

gradebook = dict()

def read_file(): #Done
    try:
        grade_book = {}
        items = []
        with open("students.file", 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line:
                    items = line.split('@')
                    key = items[0]
                    value = items[1]
                    grade_book[key] = value
            return grade_book
        
    except FileNotFoundError as e:
        with open('students.file', 'w') as file:
            file.close()
        with open("students.file", 'r') as file:
            for line in file.readlines():
                line.strip()
                items = line.split('@')
                key = items[0]
                value = items[1]
                grade_book[key] = value
            return grade_book
        
def append_file(grade_book): #Done
    with open('students.file', 'a') as file:
        for key, value in grade_book.items():
            file.write(f'{key}@{value}\n')

def write_to_file(grade_book): #Done
    with open('students.file', 'w') as file:
        for key, value in grade_book.items():
                if key and value.strip():
                    file.write(f'{key}@{value} \n')

class Student:
    def __init__(self):
        students = read_file()

        if len(students.items()) == 0:
            self.admin_no = 1

        else:
            for item in students.keys():
                key = int(item)
                self.admin_no = str(key + 1)

    def add_student(self):
        self.name = input('Enter name: ')
        loop2,loop = True, True

        while loop:
            prints = ['Maths', 'English', 'Science', 'SST']
            maths, eng, sci, sst = 0,0,0,0
            self.marks = [maths, eng, sci, sst]
            choice = input('Enter marks now? Y/N : ')
            if choice.upper() == 'N':
                loop = False
                
            elif choice.upper() == 'Y':
                try:
                    index = 0
                    for mark in self.marks:
                        while loop2:
                            mark = int(input(f'Enter marks for {prints[index]} : '))
                            if mark >= 0 and mark <= 100:
                                try:
                                    vars[index] = mark
                                except:
                                    loop = False
                                index += 1
                                if index == 4:
                                    loop2 = False
                                    loop = False
                            else:
                                loop2 = True
                except:
                    print('Invalid value entered!!')

            else:
                print('Invalid input!!')

        grade_book[self.admin_no] = f'{self.name},{self.marks[0]},{self.marks[1]},{self.marks[2]},{self.marks[3]}'

        try:
            append_file(grade_book)

        except:
            write_to_file(grade_book)

    def delete_student(self):
                students = read_file()
                self.admin_no = input('Enter admission number : ')

                if self.admin_no in students.keys():
                    students.pop(self.admin_no)
                    write_to_file(students)

                else:
                    print('Student does not exist in gradebook!!')

    def edit_student(self):
        students = read_file()
        self.admin_no = input('Enter admission number : ')

        if self.admin_no in students.keys():
            data = ['Name', 'Maths', 'English', 'Science', 'SST']
            index = 0

            print("Admission Number cannot be modified !")
            index = 0
            for turn in data:
                print(f'{index + 1} - {turn} : ')
                index += 1

            choice = int(input('What would you like to modify : '))
            data = input('Enter new value : ')

            for key in students.keys():
                if key == self.admin_no:
                    values = students[self.admin_no]
                    values.strip()
                    items = values.split(',')
                    items[choice - 1] = data
                    students[self.admin_no] = f'{items[0]},{items[1]},{items[2]},{items[3]},{items[4]}'
                    write_to_file(students)

                else:
                    continue

        else:
            print('Student does not exist in gradebook!!')


    def view_student(self): #Done
        self.admin_no = input('Enter admission number : ')
        students = read_file()
        if self.admin_no in students.keys():
            for key in students.keys():
                if key == self.admin_no:
                    values_list = students[key]
                    values = values_list[0:-1]
                    value = values.split(',')
                    print(f'Admin no : {key}    Name : {value[0]}   Maths : {value[1]}   English : {value[2]}   Science : {value[3]}   SST : {value[4]}')

        else:
            print('Student does not exist in gradebook!!')


def stat(): #done
    students = read_file()
    
    #mean
    average_per_student = []
    maths,engs,scis,ssts = [],[],[],[]
    for key, value in students.items():
        vals = value.split(',')
        values = [int(val) for val in vals[1:5]]
        sum_marks = sum(values)
        average = sum_marks / 4
        average_per_student.append(f'{key},{average}')

        maths.append(values[0])
        engs.append(values[1])
        scis.append(values[2])
        ssts.append(values[3])
            
    sum_per_subject = [sum(maths), sum(engs), sum(scis), sum(ssts)]
    average_per_subject = [item/len(students.keys()) for item in sum_per_subject]

    #mode
    mode_maths = max(maths, key=maths.count)
    mode_engs = max(engs, key=engs.count)
    mode_sci = max(scis, key=scis.count)
    mode_sst = max(ssts, key=ssts.count)
    modes = [mode_maths, mode_engs, mode_sci, mode_sst]

    #modal frequency
    mf_maths = maths.count(mode_maths)
    mf_engs = maths.count(mode_engs)
    mf_scis = maths.count(mode_sci)
    mf_ssts = maths.count(mode_sst)
    mfs = [mf_maths, mf_engs, mf_scis, mf_ssts]



    return [average_per_student, average_per_subject, modes, mfs, maths, engs, scis, ssts]

def print_gradebook(): #Done
    students = read_file()
    for key, values in students.items():
        value = values.split(',')
        print(f'Admin no : {key}    Name : {value[0]}   Maths : {value[1]}   English : {value[2]}   Science : {value[3]}   SST : {value[4]}')

def print_menu(): #Done
    print("--------------------Menu--------------------")
    print("1 - Add student with marks")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

print(f"Welcome to students Gradebook\nBy".upper())
print(f"{your_name} - {your_reg_number}\n")

#Print menu for first time
print_menu()



#initialize the gradebook
grade_book = dict()

while True:
    choice = input("\n--------------------\nEnter your choice\n")
    
    if choice == '1':
        student = Student()
        student.add_student()#Code to add a student. Teacher/User should supply admin_no, name and optionally marks for SST, Maths, science and Eng
        print("Student added.") #Include details for added student and current number of students in grade book.
    
    elif choice == '2':
        student = Student()
        student.delete_student()#Add Code to delete a student. Teacher/User admin_no for student to delete
        print("Student deleted")
    
    elif choice == '3':
        student = Student()
        index2 = 0
        subjects = ['Maths', 'English', 'Science', 'SST']
        statistics = stat()#Add Code give the following gradebook statistics

        for subject in subjects:
            index1 = 1
            print(subject.upper())
            print(f'Mean: {format(statistics[index1][index2], '.2f')}')
            index1 += 1
            print(f"Mode: {statistics[index1][index2]}")
            index1 += 1
            print(f"Modal frequency: {statistics[index1][index2]}")
            index2 += 1

            index = 4
            for j in statistics[4:-1]:
                print(f"Lowest mark: {min(statistics[index])}")
                print(f"Highest mark: {max(statistics[index])}")

            print('------------------------------------------------------------------------------------------')
        #Repeat the above output for SST and Eng
    
    elif choice == 'm':
        print_menu()
    
    elif choice == 'c':
        os.system('cls') #Only for windows
        
    elif choice == 'q':
        print('Bye bye')
        break

    elif choice == '4':
        student = Student()
        student.view_student()

    elif choice == '5':
        student = Student()
        student.edit_student()
        print('Edit successful')

    elif choice == '6':
        print_gradebook()

    else:
        print('Invalid input!!')