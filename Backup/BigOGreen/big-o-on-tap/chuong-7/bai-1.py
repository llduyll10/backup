
ls = ['B', 'b', 'I', 'i', 'G', 'g', 'O', 'o']
mystr = input()
flag = False
for s in mystr:
	if s in ls:
		flag = True
		break
if flag:
	print("YES")
else:
	print("NO")