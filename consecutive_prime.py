
### problem 50

import math

def cal_consecutive_sum(array1, i, j):
	sum=0
	#print "i,j:%d %d "%(i,j)
	### the rule is always that the two ends:  i and j must be inclusive....so j+1 is justifiably used.
	for k in range(i, j+1, 1):
		sum += array1[k]
		if (sum>max_nos1):
			break
		#print "k:%d "%array1[k]
	return sum

def erasthotene_cross(array, n):
	for i in range(2,n,1):
		array[i]=0
	for i in range(2,n,1):
		if (array[i]==0):
			j=2*i
			while (j<n):
				array[j]=1
				j+=i
	return array

max_nos1=1000000
max_nos=max_nos1*10
array=[]

for i in range(max_nos):
	array.append(0)
	
### array=prime number
### intersperse with zero...
### if array[p]==0,p>=2 then primer number
array=erasthotene_cross(array, max_nos)

counter=1
array1=[]
### array1 = purely prime number

for i in range(2,max_nos,1):
	if (array[i]!=1):
		array1.append(i)

mylen=len(array1)

max_term=0
max_term_sum=0
#array2=[]
#array3=[]
#array4=[]

for i in range(mylen):
	print "trying...%d"%i
	for j in range(i+3,mylen,1):
		if (array1[j]>max_nos1):
			continue
		sum=cal_consecutive_sum(array1, i, j)
		if (sum>=max_nos1):
			continue
		if (array[sum]==0):
			#array2.append(i)
			#array3.append(j-i+1)
			#array4.append(sum)
#			for k in range (i,j,1):
#				print array1[k]
			print "sum: "+str(sum)+" terms: "+str(j-i+1)+" start %d %d"%(array1[i],array1[j])
			if (j-i+1>max_term):
				max_term=j-i+1
				max_term_sum=sum


print "max_term"+str(max_term)+"max_term_sum:"+str(max_term_sum)
