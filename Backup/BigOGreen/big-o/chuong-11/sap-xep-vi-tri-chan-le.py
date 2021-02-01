def insertionSort(a):
    for i in range(1,len(a)):
        x = a[i]
        j = i
        while j>0 and a[j-1] > x:
            a[j] = a[j-1]
            j -= 1
        a[j] = x

n = int(input())
a = list(map(int,input().split()))



mangChan = []
mangLe = []

for i in range(n):
    if a[i] % 2 == 0:
        mangChan.append(a[i])
    else:
        mangLe.append(a[i])

insertionSort(mangChan)
insertionSort(mangLe)

k=0 # vi tri dau tien cua mang chan
j = -1 # in mang le tu phai sang trai de co thu tu giam dan
for i in range(n):
    if a[i] % 2 == 0:
        print(mangChan[k],end=" ")
        k+=1
    else:
        print(mangLe[j],end=" ")
        j-=1