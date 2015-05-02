
nos=1929394959697989990
max_nos=int("152999925")
min_nos=int("152099025")
nos_string="1.2.3.4.5.6.7.8.9.0"

nos_string="152.99.25"

n=111
nprev=n

import re

while n*n < min_nos:
	n=n*2
n=n/2
while n*n < min_nos:
	n=n+1
print n

while n*n < max_nos:
	n=n*2
n=n/2
while n*n < max_nos:
	n=n+1
print n

raw_input()
print re.search(nos_string, str(12344*12344))

print re.search(nos_string, str(12344*12344))

while (re.search(nos_string, str(nprev*nprev))) is None:
	if (nprev*nprev>(max_nos)):
		break 
	if (n*n < max_nos) and (nprev*nprev > min_nos):
		n=(n+nprev)/2
	elif (n*n < max_nos) and (nprev*nprev > min_nos):
		nprev=n
		n=2*n
	print nprev, n, (n+nprev)/2, nprev*nprev
	print re.search(nos_string, str(nprev*nprev))
print re.search(nos_string, str(nprev*nprev))
print n
print n*n
print nprev
