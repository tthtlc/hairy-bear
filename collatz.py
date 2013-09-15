
### problem 14

import math
from fractions import Fraction

def collatz(start_nos):
	nos = start_nos
	array=[]
	while (nos!=1):
		if (nos%2==0):
			nos = nos /2
		else:
			nos = 3*nos + 1
		array.append(nos)
	return array

max_nos=1000000

min_length=max_nos
max_length=2
for start_nos in range(2,max_nos, 1):
	myarr=collatz(start_nos)
	mylen = len(myarr)
	print "chain length" + str(start_nos) + ":::"+ str(mylen)
	if (mylen>max_length):
		max_length = mylen
	if (mylen<min_length):
		min_length = mylen

print "min"+str(min_length)
print "max"+str(max_length)

##for i in range(mylen):
##      print myarr[i]
