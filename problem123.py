
import numpy

def prime_remainder(pn, n):
	remainder=((pn-1)**n + (pn+1)**n)%(pn*pn)
	return remainder


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

#plist=primesfrom2to(10000000000)
plist=primesfrom2to(100000)
print plist[1]
print plist[2]
print plist[3]
print prime_remainder(plist[3],3)
print len(plist)
print prime_remainder(plist[1000],1000)
##455052511
raw_input()

#print len(plist)

for i in range(0, len(plist)):
	print prime_remainder(plist[i],i)
