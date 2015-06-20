
import sys
from fractions import *


sum = 0
max=80
upper_bound=[0 for i in range(max)]
for i in range(max-1,0,-1):
	sum=sum+Fraction(1,i*i)
	upper_bound[i]=sum

sum=0
forward_sum=[0 for i in range(max)]
sum_cell=[0 for i in range(max)]

def forward_sum_check(index,sum):
	i=index
	before_add_sum=sum+Fraction(1,i*i)
	while (before_add_sum>0.5) and (i+1<max):
		i=i+1
		before_add_sum=sum+Fraction(1,i*i)
	if (before_add_sum==0.5):
		for j in range(max):
			if (sum_cell[j]==1):
				print j
				sum_cell[j]=0
		return 1
	else:
		if (before_add_sum+upper_bound[i]>0.5) and (i+1)<max:
			sum_cell[i]=1
			sum=before_add_sum
			forward_sum[i]=sum
			forward_sum_check(i+1,sum)
			## give up this brnach

sum=0
forward_sum=[0 for i in range(max)]
forward_sum_check(2,sum)

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
