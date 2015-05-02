
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


count=0
for j in range (0, 1000000):
	count = count + 1000000
	#for i in range (1+j*1000000,1000000+j*1000000):
	#	count = count + 1
	print count
	raw_input()

##224427

print count
