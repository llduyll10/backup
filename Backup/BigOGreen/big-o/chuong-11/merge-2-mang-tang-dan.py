def Merge(a, b, c):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1


n = int(input())
A = list(map(int, input().split(' ')))
m = int(input())
B = list(map(int, input().split(' ')))
C = [0]*(n+m)

Merge(A, B, C)
