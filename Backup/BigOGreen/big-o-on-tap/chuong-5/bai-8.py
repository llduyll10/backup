n = int(input())
a = []
b = []
for i in range(n):
    ai,bi = map(int,input().split())
    a.append(ai)
    b.append(bi)
id = 0
for i in range(n):
    if a[id] < a[i] or (a[id] == a[i] and b[id] < b[i]):
        id = i
print(id+1)