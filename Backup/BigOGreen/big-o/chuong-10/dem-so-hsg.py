class Student:
    def __init__(self,toan,van):
        self.toan = toan
        self.van = van
    def DiemTB(self):
        return (self.toan + self.van) / 2
N = int(input())
a = []
for i in range(N):
    name = input()
    toan,van = map(float,input().split())
    a.append(Student(toan,van))
res = 0
for i in a:
    if i.DiemTB() >= 9.0:
        res += 1
print(res)
