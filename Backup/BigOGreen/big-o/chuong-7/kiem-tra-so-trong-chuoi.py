myStr = input()
count = 0
for s in myStr:
    if '0' <= s <='9':
        count += 1
print(count)