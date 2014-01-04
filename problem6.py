
import math

i=1
sum_square=0
sum=0
while i <= 100:
    sum += i
    sum_square += i*i
    i = i+1
s1=sum*sum
s2=sum_square
print s1-s2
