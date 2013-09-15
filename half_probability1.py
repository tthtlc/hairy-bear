
from bigfloat import *
import math
import sys

## printing all numbers that satisfy 2f^2-1=odd square number

## any number that satisfy (2d-1)^2=2f^2-1??? for any d>10^12???

d=10**12
print d
total=10**8
for i in range(total):
	a=(2*d-1)
	b=a*a
	b=(b+1)/2
	b1=math.sqrt(b)
	b2=int(b1)
	if (b2==b1):
		print "ans d %d  b2*b2=%d==%d=b=%d  "%(d, b2*b2, b1*b1, b)
	d=d+i
	
