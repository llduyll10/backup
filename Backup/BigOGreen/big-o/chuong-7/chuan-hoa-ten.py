n = int(input())

for j in range(n):
    name = input()
    res =""
    for i in range(len(name)):
        if i == 0 or name[i-1] == ' ':
            if 'a' <= name[i] <= 'z' :
                res += chr(ord(name[i]) - 32)
            else:
                res += name[i]
        else:
            if 'A' <= name[i] <= 'Z' :
                res += chr(ord(name[i]) + 32)
            else:
                res += name[i]
    print(res)
