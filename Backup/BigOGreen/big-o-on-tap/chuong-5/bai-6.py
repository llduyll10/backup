n = int(input())
a = list(map(int,input().split()))

count = 0
minVal = a[0]
for i in range(n):
    if a[i]<minVal:
        minVal = a[i]


for i in range(n):
    if a[i] > minVal:
        count += (a[i]-minVal)
print(count)
   