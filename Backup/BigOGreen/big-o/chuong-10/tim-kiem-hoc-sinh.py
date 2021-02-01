class Student:
    def __init__(self, id, math, literature):
        self.id = id
        self.math = math
        self.literature = literature

n, q = map(int, input().split(' '))
students = []
for i in range(n):
    id, math, literature = input().split(' ')
    math = float(math)
    literature = float(literature)
    new_student = Student(id, math, literature)
    students.append(new_student)

for i in range(q):
    query_id = input()
    for student in students:
        if student.id == query_id:
            print(student.math, student.literature)
            break