def DemSLChuSo(n):
    if n < 10:
        return 1
    return  1 + DemSLChuSo(n//10)

n = int(input())

if n<0:
    print(DemSLChuSo(-n))
else:
    print(DemSLChuSo(n))