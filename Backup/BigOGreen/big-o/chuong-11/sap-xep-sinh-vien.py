#Sap xep tu lon de nho
class SinhVien():
    def __init__(self,id,diem):
        self.id = id
        self.diem = diem


n,m  = map(int,input().split(' '))
SV = []
for i in range(n):
    id, diem = map(float,input().split())
    diem = float(diem)
    id = int(id)
    SV.append(SinhVien(id,diem))
for i in range(1,n):
    j = i
    x = float(SV[i].diem)
    temp = SV[i]
    while j>0 and float(SV[j-1].diem) < x:
        if(SV[j-1].diem == SV[j].diem and SV[j-1].id > SV[j].id): #neu la = nhau thi xet id
           SV[j-1] = SV[j]
        else:
            SV[j] = SV[j-1]
        j-=1
    SV[j] = temp


for i in range(m):
    print(SV[i].id)






