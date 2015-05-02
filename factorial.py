
def factorial(n):
	if n==1:
		return 1
	else:
		return factorial(n-1)*n

ans=str(factorial(100))

sum=0
for x in ans:
	sum=sum+int(x)

print sum

#print factorial(10)
