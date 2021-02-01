m,n = map(int,input().split())
a = list(map(int,input().split()))

ans = "-1"

for i in range(0,m):
    if a[i] == n:
        ans = i + 1

print(ans)