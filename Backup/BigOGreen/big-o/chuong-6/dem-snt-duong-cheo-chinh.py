def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
#Duong cheo chinh => i=j
m = int(input())
a =[]
for i in range(m):
    tmp = list(map(int,input().split()))
    a.append(tmp)
count = 0
for i in range(m):
    if isPrime(a[i][i]):
        count += 1
print(count)