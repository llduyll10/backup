def Merge(A,B,C):
    i =j = k = 0
    while i<len(A) and j < len(B):
        if A[i] < B[j]:
            C[k] = B[j]
            j+=1
        else:
            C[k] = A[i]
            i += 1
        k += 1
    while i<len(A):
        C[k] = A[i]
        i+=1
        k+=1
    while j<len(B):
        C[k] = B[j]
        j+=1
        k+=1

def MergeSort(n, A):
    if n>1:
        n1 = n // 2
        n2 = n - n1
        
        L = A[:n1]
        R = A[n1:]
        #De qui 
        MergeSort(n1,L)
        MergeSort(n2,R)

        Merge(L,R,A)

n = int(input())
A = list(map(int,input().split()))

MergeSort(n,A)

for x in A:
    print(x,end=' ')

    