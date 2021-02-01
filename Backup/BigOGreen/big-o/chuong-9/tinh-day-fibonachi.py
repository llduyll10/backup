def TinhDayFibonachi(n):
    if n ==0 or n == 1:
        return 1
    return TinhDayFibonachi(n-1) + TinhDayFibonachi(n-2)

N = int(input())
print(TinhDayFibonachi(N))