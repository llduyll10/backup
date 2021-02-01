arr_adj = []
n = int(input())
for i in range(n):
    new_row = list(map(int,input().split()))
    arr_adj.append(new_row)
count = 0
arrEge = [[] for i in range(n)] #Tao n mang rong tu mang n nhap vao
for u in range(n):
    for v in range(n):
        if arr_adj[u][v] == 1:
            arrEge[u].append(v)
            count += 1

print(count)
for u in range(n):
    for v in arrEge[u]:
        print(u,v)

