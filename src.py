from student import *

def PrintMenu() -> None:
    print('''
        1 : add
        2 : delete
        3 : search
        4 : store
        5 : quit''')

def LoadDataFromFile(fileName: str) -> StudentsMarkManager:
    ''' returns None if there's no file or the file is empty'''
    try:
        f = open(fileName, 'r')
    except OSError:
        return None

    line = f.readline().split(' ')

    if line == ['']:
        return None

    # create a new class
    s = StudentsMarkManager(
        line[0], StudentMark(*list(map(int, line[1:]))))

    # read lines untill end of the file
    while True:
        line = f.readline().split(' ')

        if line == ['']:
            break

        s.AddStudent(line[0], StudentMark(*list(map(int, line[1:]))))

    return s

def StoreDataToFile(s: StudentsMarkManager, fileName: str) -> None:
    f = open(fileName, 'w')
    students = s.GetStudents()

    if students == []:
        return

    # writes the first line without a line feed
    f.write(f'{students[0][0]} {students[0][1].mathMark} {students[0][1].englishMark} {students[0][1].koreanMark}')

    if len(students) >= 1:
        for student in students[1:]:
            f.write(f'\n{student[0]} {student[1].mathMark} {student[1].englishMark} {student[1].koreanMark}')

def Start(dataFileName: str) -> None:
    s = LoadDataFromFile(dataFileName)

    if s == None:
        isManagerPresent = False
    else:
        isManagerPresent = True

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
            if not isManagerPresent:
                print('You have to add first')
            else:
                StoreDataToFile(s, dataFileName)
        elif menu == 5:
            print('Bye')
            break
        else:
            print('invalid menu')

Start('data.txt')
