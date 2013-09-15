

def fib(n):    # write Fibonacci series up to n
	"Print a Fibonacci series up to n"
	result=[]
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result


f1000=fib(2000)
print f1000

