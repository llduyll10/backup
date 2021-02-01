def TimSoLonNhatTrongDay(n):
    if n< 10:
        return n
    return max(n%10,TimSoLonNhatTrongDay(n // 10))
N = int(input())
if N<0:
    print(TimSoLonNhatTrongDay(-N))
else:
     print(TimSoLonNhatTrongDay(N))