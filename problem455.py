

##  Let f(n) be the largest positive integer x less than 10^9 such that the last 9 digits of n^x form the number x (including leading zeros), or zero if no such integer exists.

##f(4) = 411728896 (4411728896 = ...490411728896)
##f(10) = 0
##f(157) = 743757 (157743757 = ...567000743757)
##  sum(f(n)), 2< n<  103 = 442530011399
##Find sum(f(n)), 2  n  106.

print 411728896, 4411728896 %1000000000, 490411728896%1000000000
print 10**9

max_modulo=10**9

def f(x):
	prod=1
	for i in range(1,10**8):
		prod *= x
		if (prod == i):
			return prod
		if (prod > max_modulo):
			prod %= max_modulo
	return prod

print f(157)
print f(4)
