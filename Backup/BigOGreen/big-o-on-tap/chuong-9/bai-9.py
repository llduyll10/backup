def UCLN(a,b):
    if b == 0:
        return a
    return UCLN(b,a%b)

a,b = map(int,input().split())
print(UCLN(a,b))