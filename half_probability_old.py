

import math

def first_func(x,y):
	diff=x*x-x-2*x*y-y*y+y
	return diff

def root_generator(d):
	x=(1+sqrt(1+2*d*(d-1)))/2
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
total=1000000000000000
end_nos=707540000000
end_nos=707107000000
end_nos=707106800000
end_nos=707106781192
end_nos=707106781188
counter=start_nos
prev_x=0
prev_y=0
my_prev_diff=999
step=10
max_counter=10000

fo



while (itotal<total+max_counter):
	print root_generator(itotal)
	itotal+=step




	while (step>1):
		while(counter<end_nos):
		##for counter in range(start_nos, total, 1):
			x=counter
			y=total-x
			mydiff=first_func(x,y)
			print mydiff, x, y, step
			if (mydiff>0)&(my_prev_diff<0):
				start_nos=prev_x
				end_nos=x
				break
			#if (mydiff<10)&(mydiff>-10):
			#	print mydiff, x, y
			counter+=step
			prev_x=x
			prev_y=y
			my_prev_diff=mydiff
		counter=start_nos
		prev_x=0
		prev_y=0
		step = step / 2
	step=10
	total+=10
