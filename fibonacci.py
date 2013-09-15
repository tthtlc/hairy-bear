import math

first=1
second=2
next=0
sum=0

while (second<=4000000):
	next=first+second
	if (second%2==0):
		sum+=second
		print sum, second
	first=second
	second=next
print sum
