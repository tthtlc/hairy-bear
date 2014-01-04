

# problem 16

ans=2**1000
mystring=str(ans)
### print mystring
sum=0
for mylength in range(len(mystring)):
	sum += int(mystring[mylength])

print sum
