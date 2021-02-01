class NhanVien():
    def __init__(self,id,ten,nam_sinh):
        self.id = id
        self.ten = ten
        self.nam_sinh = nam_sinh

n = int(input())
A = []

#APPEND tung nhan vien vao mang
for i in range(n):
    id,ten,nam_sinh = input().split(' ')
    nam_sinh = int(nam_sinh)
    nv = NhanVien(id,ten,nam_sinh)
    A.append(nv)

old_nv = A[0]

for i in range(1,n):
    if A[i].nam_sinh < old_nv.nam_sinh or (A[i].nam_sinh == old_nv.nam_sinh and A[i].id < old_nv.id):
        old_nv = A[i]
print(old_nv.id,old_nv.ten,old_nv.nam_sinh)