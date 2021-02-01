class PhanSo():
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def UCLN(self):
        a = self.tu
        b = self.mau
        while(b != 0):
            r = a % b
            a = b
            b = r
        return a
    def RutGon(self):
        UCLN = self.UCLN()
        self.tu //= UCLN
        self.mau //= UCLN
    def SoSanh(self,other):
        return self.tu * other.mau - self.mau * other.tu

n = int(input())

A = []
for i in range(n):
    x,y = map(int,input().split())
    A.append(PhanSo(x,y))
res = A[0] #Gia su A[0] la max
for i in range(1,n):
    if(res.SoSanh(A[i]) <= 0):
        res = A[i] #A[i] > A[0] => A[i] la max

res.RutGon()
print(res.tu, res.mau)
    