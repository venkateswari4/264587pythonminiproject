all_students = []


def markssum(mark1, mark2, mark3):
    return mark1 + mark2 + mark3


def avg(total):
    return total / 3


def search(all_students, r):
    f = 0
    for student in all_students:
        if student['Rollno'] == r:
            f = 1
            for key, value in student.items():
                print('{0}: {1}'.format(key, value))
    if f == 0:
        print('No such record')


def details():
    n = int(input("Please enter number of students:"))
    for i in range(0, n):
        print('enter details of student', i + 1)
        stud_name = input('Enter the name of student: ')
        stud_rollno = int(input('Enter the roll number of student: '))
        mark1 = int(input('Enter the marks in subject 1: '))
        mark2 = int(input('Enter the marks in subject 2: '))
        mark3 = int(input('Enter the marks in subject 3: '))
        total = markssum(mark1, mark2, mark3)
        average = avg(total)
        all_students.append({
            'Name': stud_name,
            'Rollno': stud_rollno,
            'Mark1': mark1,
            'Mark2': mark2,
            'Mark3': mark3,
            'Total': total,
            'Average': average
        })


def getalldetails(all_students):
    i = 1
    for student in all_students:
        print('Student', i, 'details:')
        for key, value in student.items():
            print('{0}: {1}'.format(key, value))
        i += 1


def select():
    print('select the option Enter 1 or 2 or 3')
    print('1.get details of all students 2.search for a student information 3.exit')
    t = int(input())
    if t == 1:
        getalldetails(all_students)
        print('Want to perform some other operation?? Y or N: ')
        inp = input()
        if inp == 'Y':
            select()
        exit()
    elif t == 2:
        print("Enter roll number to search")
        r = int(input())
        search(all_students, r)
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y':
            select()
        exit()
    else:
        exit()


print('Student information system')
print('Enter the student details')
details()
select()

