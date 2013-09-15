

import math

def first_func(x,y):
	diff=x*x-x-2*x*y-y*y+y
	return diff

def second_func(x,d):
	diff=2*x*x-2*x-d*d+d
	return diff

def root_generator(d):
	x=(1+math.sqrt(1+2*d*(d-1)))/2
	return x

##print first_func(15,6)
##print "ahaha"

##for total in range(1, 21,1):
##	tmptotal=total*1	

total=1000000000
max_counter=1000000000
total+=max_counter
total+=max_counter

step=1
itotal=total

while (itotal<total+max_counter):
	n=root_generator(itotal)
	n1=int(n)
	if (n1==n):
		x=n1
		y=itotal-x
		##print second_func(x,itotal)
		#print 'ffff:%20.10f '%(n1)
		diff=second_func(x,itotal)
		print diff
		#print "ooo"
		#print second_func(x,itotal+1)
		#print second_func(x+1,itotal)
		#print "ooo"
		#print second_func(x,itotal-1)
		#print second_func(x-1,itotal)
		if (diff==0):
			print 'blue:%20.0f total:%20.0f'%(n1,itotal)
##		if (first_func(x,y)==0):
##			print '%20.10f '%(n1)
#		if (icount>1000000):
#			print icount+jcount
#			jcount+=icount
#			icount=0
	itotal+=step
