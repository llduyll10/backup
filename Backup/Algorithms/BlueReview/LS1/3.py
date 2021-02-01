n = int(input())
v = list(map(int, input().split(' ')))

time = 0
for i in range(n):
    if time + 15 < v[i]:
        print(time+15)
        exit()
    else:
        time = v[i]

print(min(90,time+15))