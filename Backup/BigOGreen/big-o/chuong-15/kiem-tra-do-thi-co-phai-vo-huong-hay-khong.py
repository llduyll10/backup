
#Neu la do thi vo huong => a[u][v] = a[v][u]
n = int(input())
adj_matrix = []
for x in range(n):
    new_row = list(map(int,input().split()))
    adj_matrix.append(new_row)

flag = True
for u in range(n):
    for v in range(u+1,n):
        if adj_matrix[u][v] != adj_matrix[v][u]:
            flag = False

if flag:
    print('YES')
else:
    print('NO')