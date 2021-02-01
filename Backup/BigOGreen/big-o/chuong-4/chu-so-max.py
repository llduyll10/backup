def maxDigit(n):
    ans = -1
    while n > 0:
        if ans < n % 10: #chia lay du
            ans = n % 10
        n = n // 10 # chia lay nguyen
    return ans

n = int(input())
print(maxDigit(n))