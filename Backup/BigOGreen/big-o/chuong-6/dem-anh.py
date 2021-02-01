m,n = map(int,input().split())
a = []
for i in range(m):
    tmp = list(map(int,input().split()))
    a.append(tmp)
count = 0
for i in range(m):
    for j in range(n):
        if a[i][j] > 100:
            count += 1
print(count)
