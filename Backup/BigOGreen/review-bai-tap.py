def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1,1):
        if n%i == 0 :
            return False
    return True
n,m = map(int,input().split())
a = []
for i in range(m):
    tmp = list(map(int,input().split()))
    a.append(tmp)
count = 0
 for i in range(m):  
    if isprime(a[i][0]):  
        cnt += 1  
    if isprime(a[i][n - 1]):  
        cnt += 1  
  
for j in range(1, n - 1):  
    if isprime(a[0][j]):  
        cnt += 1  
    if isprime(a[m - 1][j]):  
        cnt += 1  
  
print(cnt)