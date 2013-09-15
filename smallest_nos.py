
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



flag=1
nos=0
while (flag==1):
	nos=nos+1
	flag=0
	##print nos
	for i in range(1,21):
		if (nos%i!=0):
			flag=1
			break
	
print nos
