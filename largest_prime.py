
import math

orig_nos=600851475143
nos=int(600851475143/4)
print nos
nos=2*1024*1023
print nos

for i in range(nos):
	nos=2*i+1
	if (orig_nos%nos==0):
		orig_nos=int(orig_nos/nos)
		print nos, orig_nos
