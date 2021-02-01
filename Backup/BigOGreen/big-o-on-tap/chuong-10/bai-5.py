class Student:
    def __init__(self,id,toan,van):
        self.id = id
        self.toan =toan
        self.van = van
n,q = map(int,input().split(' '))
students = []

for i in range(n):
    id , toan, van = input().split(' ')
    toan = float(toan)
    van = float(van)
    student = Student(id,toan,van)
    students.append(student)

for i in range(q):
    id_query = int(input())
    for stu in students:
        if stu.id == id_query:
            print(stu.toan,stu.van)
            break
    