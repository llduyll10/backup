import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def KhoangCach(self,other):
        return ((self.x-other.x) ** 2 + (self.y-other.y) ** 2) **0.5
    def __str__(self):
        return "{:.2f} {:.2f}".format(self.x,self.y)

n = int(input())
res = 0

# Lay toa do 3 diem va tinh toan

for i in range(n):
    x,y = map(int, input().split())
    A = Point(x,y) #Toa do diem a
    x,y = map(int, input().split())
    B = Point(x,y)
    x,y = map(int, input().split())
    C = Point(x,y)

    a = B.KhoangCach(C)
    b = A.KhoangCach(C)
    c = A.KhoangCach(B)

    p = (a+b+c)/2 #nua chu vi

    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    res += area

print("%.2f" % (res))