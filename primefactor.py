
n = 600851475143*839*71
n = 632382
n = 519432
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
	 print "factor=%d"%i
	 d = 1
     i = i + 1
print (n)

