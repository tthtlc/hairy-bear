
import math

i=3
sum=0
while i < 1000:
    if ((i%5==0)|(i%3==0)):
	sum += i
        print i
    i = i+1
print sum
