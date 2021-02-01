def TimChuSoDauTien(n):
    if n<10:
        return n
    return TimChuSoDauTien(n // 10)
N = int(input())
if N<0:
   N = -1 * N
print(TimChuSoDauTien(N))