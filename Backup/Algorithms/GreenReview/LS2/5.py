u ,i = map(int, input().split())
x = int(input())

if x % u == 0 and x % i == 0:
    print('Both')
elif x % u == 0 and x % i != 0:
    print('Upan')
elif x % u != 0 and x % i == 0:
    print('Ipan')
else:
    print('No')