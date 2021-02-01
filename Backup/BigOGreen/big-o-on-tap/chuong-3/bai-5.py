flag = True
pre = 0
while True:
    cur = int(input())
    if(cur == 0):
        break
    if(cur<pre):
        flag = False
        break
    pre = cur
if(flag):
    print('YES')
else:
    print('NO')