
## problem 48
import math

sum=0
final_number=1000
for a in range(1,final_number+1):
	product = 1
	for b in range(1,a+1):
		product = product * a
		#print "x %d"%product
	product = product % 100000000000
	sum += product
	#print "sum= %d "%(sum)

print "sum= %d "%(sum)
