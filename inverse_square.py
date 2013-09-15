
import math
from fractions import Fraction

def print_string(n):
	##mylen=len(n)
	for i in range(max_nos):
		if (n[i]!=0):
			print(i)

def inv_square(n):
	return Fraction(1,n*n)

array=[]
sum = 0.0
last_nos=2
max_nos=20
last_node=[]
last_node_sum=[]

last_node.append(999)
last_node_sum.append(999)

for i in range(max_nos):
       array.append(0)

while last_nos < max_nos:
	for i in range(last_nos,max_nos,1):
		tmp_val = inv_square(i)
		tmp_sum = sum + tmp_val
		if (tmp_sum==0.5):
			print "i and ANS!!", i, tmp_sum
			sum=tmp_sum
			array[i]=1
			print_string(array)
			break
		elif (tmp_sum<0.5):
			sum = tmp_sum
			array[i]=1
			last_node.append(i)
			last_node_sum.append(sum)
			##print i,sum

		##elif (tmp_sum>0.5):
		##	print "skipping ",i, tmp_sum
	if (sum!=0.5):
		last_nos=last_node.pop()
		sum=last_node_sum.pop()
		while (last_nos+1>=max_nos)&(last_nos!=999):
			last_nos=last_node.pop()
			sum=last_node_sum.pop()
			##print_string(array)
		if (last_nos==999):
			break
		tmp_val = inv_square(last_nos)
		tmp_sum = sum - tmp_val
		sum = tmp_sum
		array[last_nos]=0
		last_nos+=1
		for j in range(last_nos, max_nos, 1):
			array[j]=0
				
print sum
