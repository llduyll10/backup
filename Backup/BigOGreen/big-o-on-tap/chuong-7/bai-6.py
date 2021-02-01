# Những kí tự in hoa ta sẽ đánh số từ 0 đến 25 theo thứ tự từ A đến Z.
# Những kí tự in thường ta sẽ đánh số từ 26 đến 51 theo thứ tự từ a đến z.
def vitri(char):
    if 'A' <=char <='Z':
        return ord(char) - ord('A')
    return ord(char)- ord('a') + 26
count = [0] * 52 # mang ky tu gom 52 phan tu la so 0
str = input()
for char in str:
    count[vitri(char)] += 1 #Neu xuat hien thi tang vi tri len 1
cnt = 0
for i in count:
    if i != 0:
        cnt +=1 #Neu ma co ky tu nao thi tang bien dem len 1
print(cnt)