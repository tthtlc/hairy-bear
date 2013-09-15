
import math
import sys

def truncate_from_left(prime_array, max_nos, n):
	mystr = str(n)
	while 

	
def erasthotene_cross(array, n):
	array = [0 for x in range(n)]
	for i in range(2,n,1):
		if (array[i]==0):
			for j in range(2*i, n, i):
				array[j]=1
	return array

max_nos=10000000
array=[]

array = [0 for x in range(max_nos)]

### intersperse with zero...
### if array[p]==0,p>=2 then primer number
print "cal prime nos"
array=erasthotene_cross(array, max_nos)

for i in range(len(array)-1, 1, -1):
	### prime nos
	if (array[i]==0):
		print "prime %d "%(i)
		if (truncate_from_left(i)==1):
			if (truncate_from_right(i)==1):
				print "prime %d "%i
