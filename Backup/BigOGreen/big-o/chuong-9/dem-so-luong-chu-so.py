def demSoLuongChuSo(n):
    if n < 10 :
        return 1
    return 1 + demSoLuongChuSo(n // 10)

N = int(input())
if N<0:
    print(demSoLuongChuSo(-N))
else:
    print(demSoLuongChuSo(N))