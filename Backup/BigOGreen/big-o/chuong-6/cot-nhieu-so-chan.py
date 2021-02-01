def count_event(a, n, row):
    cnt = 0
    for j in range(n):
        if (a[row][j] % 2 == 0):
            cnt += 1
    return cnt


a = []
m, n = map(int, input().split(' '))
for i in range(m):
    tmp = list(map(int, input().split()))
    a.append(tmp)

max_event = 0
index = -1

for i in range(m):
    cnt = count_event(a, n, i)
    if cnt > max_event:
        max_event = cnt
        index = i

print(index)