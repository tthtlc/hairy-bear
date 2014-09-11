##Consider the number 15.
##There are eight positive numbers less than 15 which are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14.
##The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14
##because
##1*1 mod 15=1
##2*8=16 mod 15=1
##4*4=16 mod 15=1
##7*13=91 mod 15=1
##11*11=121 mod 15=1
##14*14=196 mod 15=1
##Let I(n) be the largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself.
##So I(15)=11.
##Also I(100)=51 and I(7)=1.
## find sum(I(n)) for 3<=n<=2*10^7

from fractions import gcd

max_modulo=10**9

def coprime_list(x):
	colist=[]
	for i in range(1,x):
		if (gcd(i,x)==1):
			colist.append(i)
	return colist

def modulo_inverse(x,nos):
	for i in range(1,nos):
		if (i*x)%nos==1:
			return i
	
#print coprime_list(15)
#colist=coprime_list(15)


def I(x):
	colist=coprime_list(x)
	#modulo_inverse(colist[i],x)
	start=len(colist)
	#print start
	for i in range(start-1,0,-1):
	#	print colist[i], modulo_inverse(colist[i],x)
		if colist[i]==modulo_inverse(colist[i],x) and colist[i]<(x-1):
			return colist[i]
	return 1

print I(15)
print I(100)
print I(7)
mysum = 0
for i in range (3, 2*pow(10,5)+1):
	mysum1=I(i)
	mysum = mysum + mysum1
	##print mysum1
print mysum
## find sum(I(n)) for 3<=n<=2*10^7
