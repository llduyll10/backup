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

nu, de = map(int, input().split())
print("%d %d" % reduceFraction(nu, de))
