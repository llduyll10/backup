#Canh khuyen la canh co dinh dau va dinh cuoi la 1 dinh => (u,v) = (u,u) = (v,v)
class Canh:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w
arrCanh = []
n = int(input())

for i in range(n):
    u,v,w = map(int,input().split())
    arrCanh.append(Canh(u,v,w))

count = 0
tich = 1

for i in range(n):
    if arrCanh[i].u == arrCanh[i].v:
        count +=1
        tich = (tich * arrCanh[i].w) % 1000007  
if count>0:
    print(count,tich)
else:
    print(-1)

