
def mygcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
##	print (x,y)
    return x

from fractions import gcd
print gcd(20,8)
print mygcd(20,8)
print gcd(2,8)
print gcd(10,11)
print gcd(10,5)
print gcd(10,3)
print gcd(10,14)
