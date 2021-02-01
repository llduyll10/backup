n = int(input())
flag = True
for i in range(0, n):
    x = int(input())
    if (x % 2 != 0):
        flag = False
        break
if (flag):
    print("YES")
else :
    print("NO")