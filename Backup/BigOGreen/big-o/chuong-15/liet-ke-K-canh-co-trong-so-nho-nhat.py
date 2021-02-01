class Canh:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w


n, K = map(int,input().split())
arrCanh = []

def insertionSort(arrCanh):
    for i in range(1,len(arrCanh)):
        j = i
        x = arrCanh[i]
        while j>0 and arrCanh[j-1].w>x.w:
            arrCanh[j]=arrCanh[j-1]
            j-=1
        arrCanh[j]=x

for i in range(n):
    u,v,w = map(int,input().split())
    arrCanh.append(Canh(u,v,w))
insertionSort(arrCanh) #Sap xep tang dan theo trong so
for i in range(K-1,-1,-1):
    print(arrCanh[i].u,arrCanh[i].v) #In ra giam dan theo trong so
