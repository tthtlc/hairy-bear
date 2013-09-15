
import math

def i2arr(n):    # write Fibonacci series up to n
        "Print array"
        result=[]
        while n>9:
		b=n%10
                result.append(b)
		n=int(n/10)
        result.append(n)
        return result



def check_palindrom(array):    # write Fibonacci series up to n
	flag=1
	n=len(array)
	#for i in range(n/2):
	#	print array[i], i
	
	if (len(array)%2==0):
		for i in range(n/2):
			if (array[i]!=array[n-i-1]):
				flag=0
				break
	else:
		for i in range((n-1)/2):
			if (array[i]!=array[n-i-1]):
				flag=0
	return flag

max_palindrom=0
for i in range(999,2,-1):
	for j in range(999,2,-1):
		nos=i * j
		
		array=i2arr(nos)
		flag=check_palindrom(array)
	##	print nos, i, j
		if (flag==1):
			##print nos, i, j
			if (nos>max_palindrom):
				max_palindrom=nos
print max_palindrom
