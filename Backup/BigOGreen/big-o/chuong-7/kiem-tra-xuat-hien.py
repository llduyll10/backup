
ls = ['B', 'b', 'I', 'i', 'G', 'g', 'O', 'o']
myStr = input()
flag = False
for s in myStr:
    if s in ls:
        flag = True
    break
if flag:
    print('YES')
else:
    print('NO')