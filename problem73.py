
## problem 73
import math


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
#	print (x,y)
    return x

def generate_fraction(d):
	list=[]
	for dominator in range(1,d+1):
		for numerator in range(1,dominator):
			if (gcd(numerator, dominator)==1):
				list.append([numerator,dominator])
	return list

def generate_fraction_float_range(d):
	list=[]
	for dominator in range(1,d+1):
		for numerator in range(1,dominator):
			if (gcd(numerator, dominator)==1):
				mynum= (float(numerator+0.0)/dominator)
				if (mynum < 0.5) and (mynum > float(1.0/3)):
					list.append(mynum)
	return list

def generate_fraction_float(d):
	list=[]
	for dominator in range(1,d+1):
		for numerator in range(1,dominator):
			if (gcd(numerator, dominator)==1):
				list.append(float(numerator+0.0)/dominator)
	return list

def sort_fraction(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
#			print (i,j)
			(x,y)=list[i]
			(v,u)=list[j]
			if (float((x+0.0)/y)) > (float((v+0.0)/u)):
				tmp=list[i]
				list[i]=list[j]
				list[j]=tmp
	return list

def sort_fraction_float(list):
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			if (float(list[i])) > (float(list[j])):
				tmp=list[i]
				list[i]=list[j]
				list[j]=tmp
	return list

list=generate_fraction_float_range(12000)
print len(list)

count=0
for i in range(len(list)):
	if list[i]>=0.5:	
		break
	if (list[i]>float(1.0/3)):
		count+=1
	#	print list[i]
		
print count


