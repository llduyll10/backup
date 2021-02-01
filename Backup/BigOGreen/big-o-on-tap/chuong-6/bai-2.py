def isAllNegatives(m,n,a,col):
    flag = True
    for i in range(m):
        if(a[i][col]>0):
            flag=False
    return flag
a=[]
m,n = map(int,input().split())

for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

for j in range(n):
    if(isAllNegatives(m,n,a,j)):
        print(j,end=" ")