#Sap xep tang dan va giu nguyen vi tri SNT
def isPrime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def InsertionSort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i
        while j>0 and A[j-1] > x:
            A[j] = A[j-1]
            j -=1
        A[j] = x

n = int(input())
A = list(map(int,input().split()))


notPrime = []
for X in A:
    if not isPrime(X):
        notPrime.append(X)
InsertionSort(notPrime)

j = 0
for i in range(n):
    if not isPrime(A[i]):
        print(notPrime[j], end=" ")
        j+=1
    else:
        print(A[i],end=" ")
