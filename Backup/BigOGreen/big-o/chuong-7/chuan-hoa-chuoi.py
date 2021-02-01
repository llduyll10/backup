myStr = input()

res = ""
resLen = 0
needASpace = False

for s in myStr:
    if s == ' ':
        if resLen > 0:
            needASpace = True
    else:
        if needASpace:
            res += ' '
            resLen += 1
            res += s
            resLen += 1
            needASpace = False
        else:
            res += s
            resLen += 1
print(res)
