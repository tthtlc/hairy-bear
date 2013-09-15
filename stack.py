
import math

data=[]

data.append(999)

for i in range(100):
	data.append(i)

print len(data)

mydata = data.pop()

while mydata!=999:
	mydata=data.pop()
	print mydata
	

