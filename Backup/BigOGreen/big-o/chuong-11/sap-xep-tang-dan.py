def insertionSort(a): #Sap xep tang dan
    for i in range(1,len(a)):
        x = a[i]
        j = i
        while j>0 and a[j-1] > x:
            a[j] = a[j-1] #Gán lại giá trị
            j -= 1 
        a[j] = x #Cập nhật lại giá trị của a[phía sau]
n = int(input())
A = list(map(int,input().split()))

insertionSort(A)

for x in A:
    print(x,end=' ')