def TimChuSoDauTien(n):
    if n < 10:
        return n
    return TimChuSoDauTien(n//10)

n = int(input())

if n<0:
    n = -1 * n
print(TimChuSoDauTien(n))
