#Mảng wordswords chứa danh sách các từ
#Biến wordword lưu từ hiện tại

#Duyet man
#Nếu ký tự hiện tại là khoảng trắng đồng nghĩa với việc là biến wordword của ta đã chứa đủ một từ hoàn chỉnh, 
# nên ta thêm wordword vào mảng wordswords và gán wordword = “” trở về chuỗi rỗng để chứa từ mới tiếp the

#Ngược lại thì ta sẽ ghép ký tự hiện tại vào biến wordword.

str = input()
words = []
word = ''
for ch in str:
    if ch == ' ':
        words.append(word)
        word = ""
    else:
        word += ch
if len(word) > 0:
    words.append(word)
res = ""
for i in range(len(words) - 1, -1, -1):
	res += words[i] + " "

print(res)