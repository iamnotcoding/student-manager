class StudentMark:
    def __init__(self, mathMark: int, englishMark: int, koreanMark: int) -> None:
        self.mathMark = mathMark
        self.englishMark = englishMark
        self.koreanMark = koreanMark

        self.markSum = self.mathMark + self.englishMark + self.koreanMark
        self.markAvg = self.markSum / 3


class StudentNotFound(Exception):
    def __str__(self):
        return 'student not found'

class StudentsMarkManager:
    def __init__(self, name, studentMark) -> None:
        self.students = [[name, studentMark]]

    def __SortStudents(self, cmp) -> None:
        # bubble sort
        for i in range(len(self.students) - 1):
            for j in range(i - 1):
                if cmp(self.students[i], self.studnets[j]) < 0:
                    #swap
                    self.students[i], self.students[j] = self.students[j] = self.students[i]

    def __CompareByName(student1, studnet2) -> int:
        if student1[0] < studnet2[0]:
            return -1
        elif student1[0] > studnet2[0]:
            return 1
        else:
            return 0

    def __GetStudentIndexByName(self, name) -> int:
        result = None

        start = 0
        end = len(self.students) - 1

        # binary search

        while end > start:
            middle = (end + start) // 2

            if self.students[middle][0] == name:
                result = middle
                break
            elif self.students[middle][0] > name:
                end = middle - 1
            else:
                start = middle + 1

        return result

    def AddStudent(self, name, studentMark) -> None:
        self.students.append([name, studentMark])
        self.__SortStudents(self.__CompareByName)

    def DelStudentByname(self, name) -> None:
        index = self.__GetStudentIndexByName(name)

        if index == None:
            raise StudentNotFound
        else:
            del self.students[index]

    def DelLastStudent(self) -> StudentMark:
        return self.students.pop()

    def ShowStudentMark(student) -> None:
        print(f'name : {student[0]} math mark : {student[1].mathMark} english mark : {student[1].englishMark} '
              f' korean mark : {student[1].koreanMark} '
              f'mark average : {student[1].markAvg} mark sum : {student[1].markSum}')

    def ShowAllStudentsMark(self) -> None:
        for student in self.students:
            StudentsMarkManager.ShowStudentMark(student)

    def FindStudentByName(self, name) -> list[StudentMark, str]:
        result = None

        index = self.__GetStudentIndexByName(name)

        if index == None:
            raise StudentNotFound
        else:
            result = self.students[index]

        return result
