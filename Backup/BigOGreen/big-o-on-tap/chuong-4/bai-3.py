def GCD(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a

def reduceFraction(a, b):
	gcd = GCD(a, b)
	a /= gcd
	b /= gcd
	return a, b
a,b = map(int,input().split())
c,d = reduceFraction(a,b)
print("{0} {1}".format(c,d))
print("%d %d"%reduceFraction(a,b))