
from fractions import Fraction

### fn=2+1/fn+1

def myroot2(max,depth):
	if (depth==max):
		return 2.0
	else:
		return 2+1/myroot2(max,depth+1)

def myroot2v2(max,depth):
	if (depth==max):
		return Fraction(2,1)
	else:
		return Fraction(2,1)+Fraction(1,myroot2v2(max,depth+1))

def myroot2v3(max):
	cell=[2 for i in range(max+1)]
	for i in range(max):
		j=max-i
		cell[j-1]=Fraction(2,1)+Fraction(1,cell[j])
	return cell[0]

count=0
for i in range(1000):
	#mynum1=myroot2v2(i,0)-Fraction(1,1)
	mynum=myroot2v3(i)-Fraction(1,1)
	#print mynum1,mynum
	if  (len(str(mynum.numerator)) -  len(str(mynum.denominator))) > 0:
		count=count+1
print count
