
# Function to add data of new student 
def add_new_stud():
    enr = input('Enter the enrollment number : ')
    sname = input('Enter student name : ')
    mob_no = input('Enter mobile number : ')
    email = input('Enter the email : ')

    fobj = open('student_info.txt', 'a')
    fobj.write(
        enr + ',' + sname + ',' + mob_no + ',' + email + '\n'
    )
    fobj.close()
    print('New student info added succesfully')

# Function to simplify the logic of function 2nd and 3rd
def check_enr(enr):
    fobj = open('student_info.txt', 'r')
    fdata = fobj.readlines()
    fobj.close()

    ind = 0
    found = False 
    for i in fdata:
        ls = i.split(',')
        if ls[0] == enr:
            print('Student name :', ls[1])
            print('Student mobile number :', ls[2])
            print('Student email :', ls[3])
            found = True
            break
        else:
            ind += 1

    return fdata, found, ind

# Function to search for a student then display it
def search_stud():
    enr = input("Enter the student's enrollment number you want to display : ")

    data = check_enr(enr)
    found = data[1]
        
    if found == False: print('Invalid enrollment number')
    elif found == True:
        print('Student name :', )


# Function to remove student data
def remove_stud():
    enr = input("Enter the student's enrollment number you want to Remove : ")
    data = check_enr(enr)
    fdata = data[0]
    found = data[1]
    ind = data[2]

    if found == False: print('Invalid enrollment number')
    elif found == True:
        fdata.pop(ind)
        fobj = open('student_info.txt', 'w')
        fobj.writelines(fdata)
        fobj.close()

        print('Data removed succesfully')



while True:
    print('\nChoose the operation you want to perform :-')
    print(' 1 - Add new student information')
    print(' 2 - Display student information')
    print(' 3 - Remove student')
    print(' 4 - Exit')
    ch = int(input('Enter your choice : '))

    if ch == 1: add_new_stud()
    elif ch == 2: search_stud()
    elif ch == 3: remove_stud()
    elif ch == 4: exit()
    else: print('Enter valid number')
