class Tao:
    def __init__(self,kl,gt): #Khoi luong va gia tien
        self.kl = kl
        self.gt = gt
n = int(input())
A = []

#Append tao vao mang A
for i in range(n):
    x,y = map(int,input().split())
    A.append(Tao(x,y))

res = A[0]
count = 0
for i in range(1,n):
    if(A[i].kl > res.kl or(A[i].kl == res.kl and A[i].gt > res.gt)):
        res = A[i]
        count = i
print(count)