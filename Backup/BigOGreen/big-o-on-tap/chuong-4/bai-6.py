def ChuSoLonNhat(n):
    res = -1
    while n>0:
        if n%10 > res:
            res = n%10
        n //=10
    return res
n = int(input())
print(ChuSoLonNhat(n))