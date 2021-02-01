def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return  False
    return True

def Merge(A,B,C):
    i = j = k = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
    while i < len(A):
        C[k] = A[i]
        i+=1
        k+=1
    while j < len(B):
        C[k] = B[j]
        j+=1
        k+=1
def MergeSort(n,A):
    if n > 1:
        n1 = n // 2
        n2 = n -n1
        
        L = A[:n1]
        R = A[n1:]

        MergeSort(n1,L)
        MergeSort(n2,R)

        Merge(L,R,A)

n = int(input())
A = list(map(int,input().split(' ')))

noPrime = []
for x in A:
    if not isPrime(x):
        noPrime.append(x)

MergeSort(len(noPrime),noPrime)
j = 0
for i in range(n):
    if not isPrime(A[i]):
        print(noPrime[j], end=" ")
        j+=1
    else:
        print(A[i],end=" ")



