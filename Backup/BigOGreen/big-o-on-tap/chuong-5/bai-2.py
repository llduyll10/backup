n = int(input())
a = list(map(int,input().split()))
maxVal = -1
for i in range(n):
    if a[i]>maxVal:
        maxVal=a[i]

print(maxVal)