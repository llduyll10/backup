import sys
sys.setrecursionlimit(10**6)

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def viTriDauTien(a,index,n):
    if index == n:
        return -1
    if isPrime(a[index]):
        return index
    return viTriDauTien(a,index+1,n)
n = int(input())
a = list(map(int,input().split()))

print(viTriDauTien(a,0,n))


