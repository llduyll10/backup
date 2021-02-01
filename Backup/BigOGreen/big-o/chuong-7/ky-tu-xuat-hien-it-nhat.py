#lấy mã ASCII của ký tự hiện tại trừ đi mã ASCII của ký tự mốc là 'A' (hoặc 'a' nếu là chữ thường) 
#kết quả có được chính là vị trí của ký tự này trong mảng
def pos(ch):
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') 
    return ord(ch) - ord('a')

def getMinimumOccurringChar(str) :  
	count = [0] * 26  #mang count gom 26 so 0
	for ch in str : 
		count[pos(ch)] += 1  #Neu vi tri nao co xuat hien thi tang no len 1 don vi
	min = 1001  # dat gia tri mac dinh cua min la 1001
	res = ""  
	for i in range(len(count)) :  
		if (count[i] != 0 and count[i] < min) :  
			min = count[i]  #gan lai gia tri cho min
			res = chr(i + ord('A'))  #Chuyen ky tu xuat hien it nhat thanh chu hoa
	return res
n = int(input())  
for i in range(n) :  
    str = input()  
    print(getMinimumOccurringChar(str))