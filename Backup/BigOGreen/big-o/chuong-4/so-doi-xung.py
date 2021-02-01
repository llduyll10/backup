#Số đối xứng khi đảo ngược = chính nó
def reverse(n):
	ans = 0
	while n != 0:
		ans = ans * 10 + n % 10
		n = n // 10
	return ans
def isMatch(n):
    return n == reverse(n)
n = int(input())
if(isMatch(n)):
    print('YES')
else:
    print('NO')