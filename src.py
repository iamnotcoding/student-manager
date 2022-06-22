from student import *


def PrintMenu() -> None:
    print('''
        1 : add
        2 : delete
        3 : search
        4 : quit''')

def Start() -> None:
    # TODO
    # file = open('data.txt')
    
    isManagerPresent = False

    while True:
        PrintMenu()

        menu = int(input())

        if menu == 1:
            rawInput = input('enter name and marks : ').split(' ')

            if not isManagerPresent:
                s = StudentsMarkManager(rawInput[0], StudentMark(
                    *list(map(int, rawInput[1:]))))

                isManagerPresent = True
            else:
                s.AddStudent(rawInput[0], StudentMark(
                    *list(map(int, rawInput[1:]))))
        elif menu == 2:
            if not isManagerPresent:
                print('You have to add first')
                break
            else:
                name = input('enter name : ')

                try:
                    foundStudent = s.DelStudentByname(name)
                except StudentNotFound:
                    print('student not found')
        elif menu == 3:
            if not isManagerPresent:
                print('You have to add first')
                break
            else:
                name = input('enter name : ')

                try:
                    foundStudent = s.FindStudentByName(name)
                except StudentNotFound:
                    print('student not found')
                    continue
                print('found student : ', end=' ')
                StudentsMarkManager.ShowStudentMark(foundStudent)
        elif menu == 4:
             print('Bye')
             break
        else:
            print('invalid menu')

Start()
