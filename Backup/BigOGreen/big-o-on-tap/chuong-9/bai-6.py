import sys
sys.setrecursionlimit(10**6)
def TongSoChan(a,n):
    if n == 0:
        return 0
    if a[n-1] % 2 == 0:
        return a[n-1] + TongSoChan(a,n-1) #Truong hop so chan
    return TongSoChan(a,n-1) # Truong hop phan tu la so le

n = int(input())
a = list(map(int,input().split()))

print(TongSoChan(a,n))