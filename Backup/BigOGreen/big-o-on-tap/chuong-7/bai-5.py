#lấy mã ASCII của ký tự hiện tại trừ đi mã ASCII của ký tự mốc là 'A' (hoặc 'a' nếu là chữ thường) 
#kết quả có được chính là vị trí của ký tự này trong mảng
def vitri(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    return ord(char) - ord('a')
def getMinimumOccurringChar(str):
    count = [0] * 26 #mang count gom 26 so 0
    for char in str:
        count[vitri(char)] += 1 #Neu vi tri nao co xuat hien thi tang no len 1 don vi
    min = 1001
    res =""
    for i in range(len(count)):
        if count[i] != 0 and count[i]<min:
            min = count[i]
            res = chr(i + ord('A'))  #Chuyen ky tu xuat hien it nhat thanh chu hoa
    return res

n = int(input())
for i in range(n):
    str = input()
    print(getMinimumOccurringChar(str))
