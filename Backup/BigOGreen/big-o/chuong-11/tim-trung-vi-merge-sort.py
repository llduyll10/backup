def Merge(a,b,c):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i+=1
        else:
            c[k] = b[j]
            j+=1
        k+=1
    while i<len(a):
        c[k] = a[i]
        i+=1
        k+=1
    while j<len(b):
        c[k] = b[j]
        j+=1
        k+=1
def MergeSort(n,a):
    if n>1:
        n1 = n//2
        n2 = n - n1
        
        L = a[:n1]
        R = a[n1:]

        MergeSort(n1,L)
        MergeSort(n2,R)

        Merge(L,R,a)

n = int(input())
a= list(map(int,input().split()))
MergeSort(n,a)


if n % 2 != 0:
    z = int(n/2) 
    print(a[z])
else:
    z = int(n/2)
    c = ((a[z]+a[z-1])/2)
    print("{:.1f}".format(c))
