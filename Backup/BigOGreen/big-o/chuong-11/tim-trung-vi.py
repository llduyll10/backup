def insertionSort(a):
    for i in range(1,len(a)):
        x = a[i]
        j = i
        while j>0 and a[j-1]>x:
            a[j] = a[j-1]
            j-=1
        a[j]=x

n = int(input())
a = list(map(int,input().split()))
insertionSort(a)

if n % 2 != 0:
    z = int(n/2) 
    print(a[z])
else:
    z = int(n/2)
    c = ((a[z]+a[z-1])/2)
    print("{:.1f}".format(c))


