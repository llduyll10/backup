class Canh:
    def __init__(self,u,v):
        self.u = u
        self.v = v
    def __str__(self):
        return '{0} {1}'.format(self.u,self.v)

n = int(input())

adj_matrix = []
#Tao mang 2 chieu
for i in range(n):
    new_row = list(map(int,input().split()))
    adj_matrix.append(new_row)

#Tao mang danh sach canh
arrCanh = []
for u in range(n):
    for v in range(u+1,n):
        if adj_matrix[u][v] == 1:
            arrCanh.append(Canh(u,v))

print(len(arrCanh))

for canh in arrCanh:
    print(canh)