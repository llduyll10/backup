#So doi xung => khi dao nguoc lai la chinh no
def reverse(n):
    res = 0
    while n !=0:
        res = res*10 + n %10
        n = n//10
    return res

n = int(input())
if(n- reverse(n) == 0):
    print('YES')
else:
    print('NO')