str = input()
words = []
word =''

for char in str:
    if char == ' ':
        words.append(word)
        word = ''
    else:
        word += char
if len(word) > 0:
    words.append(word)
res = ""
for i in range(len(words) - 1, -1, -1):
	res += words[i] + " "

print(res)