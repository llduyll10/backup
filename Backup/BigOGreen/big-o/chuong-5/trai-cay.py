n = int(input())
a = []
b =[]
#a = mang tao
#b = mang cam
for i in range(n):
    ai,bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
id = 0
for i in range(1,n):
     if a[id] < a[i] or (a[id] == a[i] and b[id] < b[i]) :  
        id = i  
print(id +1)