# Những kí tự in hoa ta sẽ đánh số từ 0 đến 25 theo thứ tự từ A đến Z.
# Những kí tự in thường ta sẽ đánh số từ 26 đến 51 theo thứ tự từ a đến z.
def pos(s):
    if 'A' <= s <='Z':
        return ord(s) - ord('A')
    return ord(s) - ord('a') + 26

count = [0]*52
str = input()
ans = "null"

for c in str:
    idx = pos(c)
    count[idx] +=1
    if count[idx] == 2:
        ans = c
        break
print(ans)