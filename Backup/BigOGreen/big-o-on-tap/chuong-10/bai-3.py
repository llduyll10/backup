class HocSinh:
    def __init__(self,ten,diemToan,diemVan):
        self.ten = ten
        self.toan = diemToan
        self.van = diemVan
    def DiemTB(self):
        return (self.toan + self.van) / 2

n = int(input())
a = []

for i in range(n):
    ten = input()
    toan, van = map(float,input().split())
    a.append(HocSinh(ten,toan,van))
res = 0

for hs in a:
    if hs.DiemTB() >= 9.0:
        res += 1
print(res)
