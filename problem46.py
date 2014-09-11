
import math
import sys

def erasthotene_cross(array, n):
	array = [0 for x in range(n)]
	for i in range(2,n,1):
		if (array[i]==0):
			for j in range(2*i, n, i):
				array[j]=1
	return array

max_nos=1000000
array=[]

array = [0 for x in range(max_nos)]

### intersperse with zero...
### if array[p]==0,p>=2 then primer number
print "cal prime nos"
array=erasthotene_cross(array, max_nos)

prime_array=[]
### prime_array = purely prime number

print "generating prime_array"
for i in range(2,max_nos,1):
	if (array[i]!=1):
		prime_array.append(i)

final_array = [0 for x in range(max_nos)]

for i in range(1,len(prime_array),1):
	j=1
	k=prime_array[i]+2*j*j
	#print prime_array[i], i, j
	while k<max_nos:
		final_array[k]=1
		k=prime_array[i]+2*j*j
		#print prime_array[i], i, j
		j=j+1	

for i in range(2,max_nos,1):
	if final_array[i]==0 and i%2==1 and (array[i]==1):
		print i

