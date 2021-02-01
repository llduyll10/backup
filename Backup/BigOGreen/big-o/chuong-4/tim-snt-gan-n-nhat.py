def isPrime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = int(input())
n1 = n
n2 = n

# Kiem tra tu n ve sau
while isPrime(n1) == False:
    n1 -= 1
#Kiem tra tu n ve truoc
while isPrime(n2) == False:
    n2 += 1

#Kiem tra bien do gan n nhat
if n - n1 <= n2 -n:
    print(n1)
else:
    print(n2)