
import math
import sys

def erasthotene_cross(array, n):
	array = [0 for x in range(n)]
	for i in range(2,n,1):
		if (array[i]==0):
			for j in range(2*i, n, i):
				array[j]=1
	return array

max_nos1=10000
max_nos=max_nos1*10
array=[]

array = [0 for x in range(max_nos)]

### intersperse with zero...
### if array[p]==0,p>=2 then primer number
print "cal prime nos"
array=erasthotene_cross(array, max_nos)

print "copy array"
array2 = array[:]

array1=[]
### array1 = purely prime number

print "generating array1"
for i in range(2,max_nos,1):
	if (array[i]!=1):
		array1.append(i)


check_nos=1781

for i in range(len(array1)):
	if (check_nos-array1[i])<0:
		break
	print "prime %d nos %d"%(array1[i], (check_nos-array1[i])/2)
