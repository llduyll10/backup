def Merge(a,b,Temp):
    i = j = k =0
    while i < len(a) and j <len(b):
        if a[i] > b[j]: #Sap xep giam dan
            Temp[k] = a[i]
            i+=1
        else:
            Temp[k] = b[j]
            j+=1
        k+=1
    while i<len(a):
        Temp[k] = a[i]
        i+=1
        k+=1
    while j<len(b):
        Temp[k] = b[j]
        j+=1
        k+=1
m,n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

Temp = [0]*(len(a)+len(b)) #Tao 1 mang rong gom cac phan tu cua mang a va b
Merge(a,b,Temp)

print(Temp[-k-1])

