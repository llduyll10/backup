import math
a, b , c = map(float, input().split())

P = a + b + c
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print('{0:.2f} {1:.2f}'.format(P,S))