#duong cheo phu co dang j = n - 1 -i

def isPrime(n):
    if n <2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

m = int(input())
a=[]
for i in range(m):
    tmp = list(map(int,input().split()))
    a.append(tmp)
res = 1
for i in range(m):
    if isPrime(a[i][m-1-i]):
        res = res * a[i][m-1-i]
ans = ans % 1000003 # dam bao du lieu tren 1 dong
print(res)