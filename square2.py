
min_nos=1020304050607080900
max_nos=1929394959697989990
nos_string="1.2.3.4.5.6.7.8.9.0"

import re
##
##while n*n < min_nos:
##	n=n*2
##n=n/2
##while n*n < min_nos:
##	n=n+1
##print n
##nprev=n
##
##while n*n < max_nos:
##	n=n*2
##n=n/2
##while n*n < max_nos:
##	n=n+1
##print n


nprev=1010101011+1
n=1389026624

print n*n
raw_input()

while (re.search(nos_string, str(nprev*nprev))) is None:
	nprev=nprev+2
	if (nprev>n):
		break
#	if (nprev*nprev>(max_nos)):
#		break 
print re.search(nos_string, str(nprev*nprev))
print n
print n*n
print nprev
