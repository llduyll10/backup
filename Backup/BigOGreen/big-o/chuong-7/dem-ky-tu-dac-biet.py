# Những kí tự in hoa ta sẽ đánh số từ 0 đến 25 theo thứ tự từ A đến Z.
# Những kí tự in thường ta sẽ đánh số từ 26 đến 51 theo thứ tự từ a đến z.

def pos(ch):
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') 
    return ord(ch) - ord('a') + 26
count = [0] * 52 # mang ky tu gom 2 phan tu
str = input()
for ch in str:
    count[pos(ch)] += 1 #Neu xuat hien thi tang vi tri len 1
cnt = 0
for e in count:
    if e != 0: #Neu ma co ky tu nao thi tang bien dem len 1
        cnt += 1
print(cnt)
