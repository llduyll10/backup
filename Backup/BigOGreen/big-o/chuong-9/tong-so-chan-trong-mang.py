import sys
sys.setrecursionlimit(10**6)
def TongSoChanTrongMnag(a,n):
    if n == 0:
        return 0
    if a[n-1] % 2 == 0:
        return a[n-1] + TongSoChanTrongMnag(a,n-1) #Truong hop so chan
    return TongSoChanTrongMnag(a,n-1) # Truong hop phan tu la so le

N = int(input())
a = list(map(int,input().split()))

print(TongSoChanTrongMnag(a,N))