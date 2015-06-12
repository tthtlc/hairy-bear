
import sys
from fractions import *


sum = 0
max=80
upper_bound=[0 for i in range(max)]
for i in range(max-1,0,-1):
	sum=sum+Fraction(1,i*i)
	upper_bound[i]=sum
	print i

for i in range(max):
	print upper_bound[i]*1.0

sys.exit(0)

for i in range(max-1,1,-1):
	cell[max-1-i]=Fraction(1,i*i)
	print i, sum*1.0, sum
for j in range(max):
	before_sum=0
	cell_array=[]
	for i in range(max):
		sum = before_sum + cell[i]
		if (sum==Fraction(1,2)):
			cell_array.append(i)
			print cell_array
		elif (sum<Fraction(1,2)):
			before_sum=sum
			cell_array.append(i)
		elif (sum>Fraction(1,2)):
			###
			print "nothing"



### algo:   if (0.5-partial_sum[i])<upper_bound[i]) then continue search else stop searching
