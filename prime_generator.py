
### problem 7

import math

def erasthotene_cross(array, n):
	for i in range(2,n,1):
		if (array[i]==0):
			j=2*i
			while (j<n):
				array[j]=1
				j+=i
	return array

max_nos=1000000
array=[]

for i in range(max_nos):
	array.append(0)
	
array=erasthotene_cross(array, max_nos)

counter=1

for i in range(2,max_nos,1):
	if (array[i]!=1):
		print i 
		if (counter==10001): 
			break
		counter+=1
