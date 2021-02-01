n = int(input())
a = list(map(int,input().split()))

boy = 0
girl = 0
for i in range(n):
    if a[i] == 0:
        boy +=1
    else:
        girl +=1
if boy == girl:
    print('YES')
else:
    print('NO')