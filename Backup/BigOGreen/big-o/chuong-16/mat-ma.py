
str = input()
s1 = []
s2 = []
tmp = [""] * len(str)

for i in range(len(str)):
    if i % 2 != 0:
        s2.append(str[i])
    else:
        s1.append(str[i])

reverseS2 = []
for i in range(len(s2)-1,-1,-1):
    reverseS2.append(s2[i])
l = 0
m = 0
for i in range(0,len(str)):
    if i%2 == 0:
        tmp[i] = s1[l]
        l+=1
    else:      
        for k in range(0,len(reverseS2)):
            tmp[i] = reverseS2[m]
            m+=1
            break

for x in tmp:
    print(x,end="")