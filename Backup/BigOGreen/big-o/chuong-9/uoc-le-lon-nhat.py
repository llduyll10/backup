def uocLeLonNhat(x,n):
    if n % 2 == 1 and x % n == 0: #Dieu kien dung de qui
        return int(n)
    return uocLeLonNhat(x,n // 2)

N = int(input())

print(uocLeLonNhat(N,N))