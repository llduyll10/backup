n = int(input())
a = list(map(int,input().split()))

# 0=> Tin hoc
# 1=> Anh van

#Neu gio cuoi cung la Tin hoc => False
if(a[-1] == 0):
    print('NO')
else:
    isGood = True
    for i in range(n-3):
        if a[i] == a[i + 1] == a[i + 2] == a[i + 3] == 0:
            isGood = False
            break
    if(isGood):
        print('YES')
    else:
        print('NO')
    
