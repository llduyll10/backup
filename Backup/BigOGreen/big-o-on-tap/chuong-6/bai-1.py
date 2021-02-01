m,n = map(int,input().split())
a=[]
for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)
for i in range(m):
    sum=0
    for j in range(n):
        sum+=a[i][j]
    print("{0}: {1}".format(i,sum))