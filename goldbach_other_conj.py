
### problem 46
### still unsolved.

import math
import sys

def cal_special_goldbach(prime, mynum):
	sum=prime+2*mynum*mynum
	#print "i,j:%d %d "%(i,j)
	### the rule is always that the two ends:  i and j must be inclusive....so j+1 is justifiably used.
	return sum


#	for k in range(i, j+1, 1):
#		sum += array1[k]
#		if (sum>max_nos1):
#			break
#		#print "k:%d "%array1[k]
#	return sum

def erasthotene_cross(array, n):
	#for i in range(2,n,1):
	#	array[i]=0
	array = [0 for x in range(n)]
	for i in range(2,n,1):
		if (array[i]==0):
			for j in range(2*i, n, i):
				array[j]=1
#				print j
			##j=2*i
			##while (j<n):
			#	j+=i
	##return array

max_nos=100000000
array=[]
max_cal_goldbach=1

array = [0 for x in range(max_nos)]

##for i in range(max_nos):
##	array.append(0)
	
### array=prime number
### intersperse with zero...
### if array[p]==0,p>=2 then primer number
print "cal prime nos"
erasthotene_cross(array, max_nos)

print "copy array"
array2 = array[:]

array1=[]
### array1 = purely prime number

print "generating array1"
for i in range(2,max_nos,1):
	if (array[i]!=1):
		array1.append(i)
#		print i


def cal_box_of_number(array, array1, lengthx, lengthy, startx, starty):
	global max_cal_goldbach
	if (startx+lengthx>=mylen):
		return 
	for j in range(starty, starty+lengthy):
		for i in range(startx, startx+lengthx):
			if (i>=mylen):
				break
			goldbach_special=cal_special_goldbach(array1[i], j)
			print "gold=%d prime %d square %d"%(goldbach_special, array1[i], j)
			if (goldbach_special<max_nos):
				if (goldbach_special>max_cal_goldbach):
					max_cal_goldbach=goldbach_special
				if (array[goldbach_special]==1):   #composite number	
					array2[goldbach_special]=0
			else:
				break
#	if (i<mylen):	
#		return cal_special_goldbach(array1[i], j)
#	else:
#		return -1

def print_goldbach_array(array2, max_goldbach):
	print ""
	for i in range(1, max_goldbach):
		if (i%2==1)&(array2[i]==1)&(array[i]==1):
			sys.stdout.write(str(i) + " ")
	print ""


mylen=len(array1)
lengthx=mylen
lengthy=int(math.sqrt(max_nos))

###maxk=int(max_nos/lengthx)

print "cal first box "
cal_box_of_number(array, array1, lengthx, lengthy, 1, 1)

print "print goldbach array %d"%max_cal_goldbach
print_goldbach_array(array2, max_nos)
