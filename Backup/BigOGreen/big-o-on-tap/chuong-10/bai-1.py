def UCLN(a,b):
    while(b != 0):
        r = a%b
        a = b
        b = r
    return a

class PhanSo:
    def __init__(self,tu,mau=1):
        self.tu = tu
        self.mau = mau
    def CongPhanSo(self,ps):
        a = self.tu * ps.mau + self.mau * ps.tu
        b = self.mau * ps.mau
        return PhanSo(a,b)
    def ToiGian(self):
        uc = UCLN(self.tu,self.mau)
        self.tu //= uc
        self.mau //= uc

x,y = map(int,input().split(' '))
a = PhanSo(x,y)

x,y = map(int,input().split(' '))
b = PhanSo(x,y)

c = a.CongPhanSo(b)
c.ToiGian()

print(c.tu,c.mau)

