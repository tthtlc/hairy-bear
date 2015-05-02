import sys


first=0
with open('/tmp/data') as f:
    for line in f:
    	#print int(line)
	second=int(line)
	if (first==0):
		first=int(line)
	else:
		print second-first
		first=second
       	if 'str' in line:
          break
    #for x in f.readline():
#	print x
    #w, h = [int(x) for x in f.readline()]

#with open('/tmp/data') as f:
#    w, h = [int(x) for x in f.readline().split()]
#    array = [[int(x) for x in line.split()] for line in f]

