m,n = map(int,input().split())
a=[]

for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

count = 0
for i in range(m):
    for j in range(n):
        if(a[i][j]>100):
            count+=1

print(count)