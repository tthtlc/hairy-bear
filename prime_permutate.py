
import math
import sys

def check_string_membership(i,j,k):
	istr=str(i)
	temp=[0 for x in range(0,26)]
	temp[int(istr[0])]+=1
	temp[int(istr[1])]+=1
	temp[int(istr[2])]+=1
	temp[int(istr[3])]+=1
	jstr=str(j)
	if (temp[int(jstr[0])]==0):
		return 0
	if (temp[int(jstr[1])]==0):
		return 0
	if (temp[int(jstr[2])]==0):
		return 0
	if (temp[int(jstr[3])]==0):
		return 0
	kstr=str(k)
	if (temp[int(kstr[0])]==0):
		return 0
	if (temp[int(kstr[1])]==0):
		return 0
	if (temp[int(kstr[2])]==0):
		return 0
	if (temp[int(kstr[3])]==0):
		return 0
	temp[int(jstr[0])]-=1
	temp[int(jstr[1])]-=1
	temp[int(jstr[2])]-=1
	temp[int(jstr[3])]-=1
	if (temp[int(jstr[0])]!=0):
		return 0
	if (temp[int(jstr[1])]!=0):
		return 0
	if (temp[int(jstr[2])]!=0):
		return 0
	if (temp[int(jstr[3])]!=0):
		return 0
	temp[int(istr[0])]+=1
	temp[int(istr[1])]+=1
	temp[int(istr[2])]+=1
	temp[int(istr[3])]+=1
	temp[int(kstr[0])]-=1
	temp[int(kstr[1])]-=1
	temp[int(kstr[2])]-=1
	temp[int(kstr[3])]-=1
	if (temp[int(kstr[0])]!=0):
		return 0
	if (temp[int(kstr[1])]!=0):
		return 0
	if (temp[int(kstr[2])]!=0):
		return 0
	if (temp[int(kstr[3])]!=0):
		return 0
	return 1
	
def erasthotene_cross(array, n):
	array = [0 for x in range(n)]
	for i in range(2,n,1):
		if (array[i]==0):
			for j in range(2*i, n, i):
				array[j]=1
	return array

### all 4 digits
min_nos=1001
max_nos=10000
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

print "calculate diff for all 4 digit prime"
for i in range(min_nos,max_nos,2):
	if (array[i]==0):
		anchor=i
		for j in range(i+2,max_nos,2):
			if (array[j]==0):
				diff=j-i
				if (diff+j<max_nos):
					if (array[j+diff]==0):
						if (check_string_membership(i,j,j+diff)):
							print "found:  %d %d %d"%(i, j, j+diff)

