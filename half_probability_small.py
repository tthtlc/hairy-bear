

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
start_nos=612493000000
start_nos=707106000000
start_nos=707106600000
start_nos=707106781184
start_nos=707106781186
total=1000000000
total=2
end_nos=707540000000
end_nos=707107000000
end_nos=707106800000
end_nos=707106781192
end_nos=707106781188
counter=start_nos
prev_x=0
prev_y=0
my_prev_diff=999
step=1
max_counter=1000000000

itotal=total
icount=0
jcount=0

while (itotal<total+max_counter):
	n=root_generator(itotal)
	n1=int(n)
	if (n1==n):
		x=n1
		y=itotal-x
		icount+=1
		##print second_func(x,itotal)
		#print 'ffff:%20.10f '%(n1)
		if (second_func(x,itotal)==0):
			print 'blue:%20.0f total:%20.0f'%(n1,itotal)
##		if (first_func(x,y)==0):
##			print '%20.10f '%(n1)
		if (icount>1000000):
			print icount+jcount
			jcount+=icount
			icount=0
	itotal+=step
print itotal
print icount
