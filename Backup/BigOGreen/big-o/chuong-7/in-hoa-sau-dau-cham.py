str = input()
res = ''
for i in range(len(str)):
    if i>=2 and str[i-2]=='.' and str[i-1]==' ' and str[i]>='a' and str[i]<='z':
        res += chr(ord(str[i]) - ord('a') + ord('A')) #Viet hoa ky tu
    else:
        res += str[i]
print(res)