class Point():
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def KhoangCach(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
    def clone(self): #Tao ra 1 Point moi tu point cu => deep clone
        temp = Point(self.x,self.y)
        return temp

x,y = map(int,input().split())
M = Point(x,y)
n = int(input())

a = []

for i in range(n):
    x,y = map(int,input().split())
    a.append(Point(x,y)) #append tung diem vao mang a

maxLength = 0
clonePoint = M.clone()
for item in a:
    current = M.KhoangCach(item) #khoang cach tu M den day so
    if current > maxLength:
        maxLength = current
        clonePoint = item

print(clonePoint.x,clonePoint.y)