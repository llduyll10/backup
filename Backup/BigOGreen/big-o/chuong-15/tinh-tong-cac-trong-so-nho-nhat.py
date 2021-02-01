class Canh:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w # w la trong so
    
n = int(input())
arrCanh = []
for i in range(n):
    u,v,w = map(int,input().split())
    arrCanh.append(Canh(u,v,w))

minw = arrCanh[0].w
for i in range(1,n):
    if minw > arrCanh[i].w:
        minw = arrCanh[i].w
sum = 0
for i in range(n):
    if arrCanh[i].w == minw:
        sum+= arrCanh[i].w
print(sum)