def giaiThua(n):
    if n == 0 or n ==1:
        return 1
    return n * giaiThua(n-1)
n = int(input())
res = giaiThua(n)
print(res)