m, n  = map(int,input().split())
a = []

#Doc ma tran
for i in range(m):
    tmp = list(map(int,input().split()))
    a.append(tmp)
for i in range(m):
    sum = 0
    for j in range(n):
        sum+= a[i][j]
    print("{0}:{1}".format(i,sum))  