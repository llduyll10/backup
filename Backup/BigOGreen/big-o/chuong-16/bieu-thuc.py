a = int(input())
b = int(input())
c = int(input())

res = [0 for i in range(6)]

res[0] = a + b + c
res[1] = a * b * c
res[2] = a + b * c
res[3] = a * b + c
res[4] = (a + b) * c
res[5] = a * (b + c)
ans = 0
for x in res:
    if x > ans:
        ans = x
    
print(ans)