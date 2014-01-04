import math

# problem 25

first=1
second=1
next=0
sum=0
counter=2

while (len(str(next))<1001):
	next=first+second
	counter += 1
	if (len(str(next))==1000):
		print counter	
	first=second
	second=next
