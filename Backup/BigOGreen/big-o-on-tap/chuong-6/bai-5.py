def demSoChanTrenRow(a,n,row):
    count = 0
    for i in range(n):
        if(a[row][i] % 2 ==0):
            count +=1
    return count

m,n = map(int,input().split())
a = []

for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

index = -1
maxCount = 0
for i in range(m):
    count = demSoChanTrenRow(a,n,i)
    if count>maxCount:
        maxCount = count
        index = i

print(index)


