
## problem 9
import math

# a < c
# b < c
# a^2 + b^2 = c^2
# smallest c=> when a=b=333.333 or 333, so c=334
# max a=b=333


for a in range(1,433):
	for b in range(1,433):
		csquare = a*a + b*b
		c = int(math.sqrt(csquare))
		if (c*c == csquare) and (1000 - c == a + b):
			print "answer= %d %d %d sum=%d product=%d"%(a,b,c, a+b+c, a*b*c)
