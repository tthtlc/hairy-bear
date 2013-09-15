#!/usr/bin/python

### problem 43

import string

def get_divisible_set(n):
	myset=[]
	for i in range(2,999):
		if (i%n==0):
			myset.append(str(i).zfill(3))
			###myset.append(str.format("%03d", i))
###n = '4'
###>>> print n.zfill(3)
###>>> '004'
	return myset

def check_adjoining_item(a, b):
	if ((a[1]==b[0])and(a[2]==b[1])):
		return 1
	else:
		return 0

def get_adjoining_set(seta, setb):
	myset=[]
	#### assuming setb is the smaller set....
	mylenb=len(setb)
	mylena=len(seta)
	for i in range(mylenb):
		for j in range(mylena):
			###print seta[j], setb[i]
			mysettmp=set(seta[j])
			mysettmp=mysettmp.union(set(setb[i]))
			if (check_adjoining_item(seta[j], setb[i])==1) and (len(mysettmp)==4):
				myset.append((seta[j],setb[i]))
	return myset


myset17=get_divisible_set(17)
myset13=get_divisible_set(13)
myset11=get_divisible_set(11)

myset=get_adjoining_set(myset13, myset17)

nextset=[]
for i in range(len(myset)):
	#print myset[i]
	(a,b)=myset[i]
	tmp=[]
	mysettmp=set()
	tmp.append(a)
	tmpset=get_adjoining_set(myset11, tmp)
	if len(tmpset)>0:
		for j in range(len(tmpset)):
			(c,d)=tmpset[j]
			mysettmp=set(d)
			mysettmp=mysettmp.union(set(c))
			mysettmp=mysettmp.union(set(a))
			mysettmp=mysettmp.union(set(b))
			if len(mysettmp)==5:
				nextset.append((c,a,b))

print "aaaa"
print nextset

myset7=get_divisible_set(7)

nextset1=[]

for i in range(len(nextset)):
	(a,b,c)=nextset[i]
	tmp=[]
	mysettmp=set()
	tmp.append(a)
	tmpset=get_adjoining_set(myset7, tmp)
	if len(tmpset)>0:
		for j in range(len(tmpset)):
			(d,e)=tmpset[j]
			mysettmp=set(e)
			mysettmp=mysettmp.union(set(d))
			mysettmp=mysettmp.union(set(a))
			mysettmp=mysettmp.union(set(b))
			mysettmp=mysettmp.union(set(c))
			if len(mysettmp)==6:
				nextset1.append((d,e,b,c))

print "bbb"
print nextset1

myset5=get_divisible_set(5)

nextset2=[]

for i in range(len(nextset1)):
	(a,b,c,d)=nextset1[i]
	tmp=[]
	mysettmp=set()
	tmp.append(a)
	tmpset=get_adjoining_set(myset5, tmp)
	if len(tmpset)>0:
		for j in range(len(tmpset)):
			(e,f)=tmpset[j]
			mysettmp=set(f)
			mysettmp=mysettmp.union(set(e))
			mysettmp=mysettmp.union(set(a))
			mysettmp=mysettmp.union(set(b))
			mysettmp=mysettmp.union(set(c))
			mysettmp=mysettmp.union(set(d))
			if len(mysettmp)==7:
				nextset2.append((e,a,b,c,d))

print "bbb"
print nextset2

myset3=get_divisible_set(3)

nextset3=[]

for i in range(len(nextset2)):
	(a,b,c,d,e)=nextset2[i]
	tmp=[]
	mysettmp=set()
	tmp.append(a)
	tmpset=get_adjoining_set(myset3, tmp)
	if len(tmpset)>0:
		for j in range(len(tmpset)):
			(f,g)=tmpset[j]
			mysettmp=set(g)
			mysettmp=mysettmp.union(set(f))
			mysettmp=mysettmp.union(set(a))
			mysettmp=mysettmp.union(set(b))
			mysettmp=mysettmp.union(set(c))
			mysettmp=mysettmp.union(set(d))
			mysettmp=mysettmp.union(set(e))
			if len(mysettmp)==8:
				nextset3.append((f,a,b,c,d,e))

myset2=get_divisible_set(2)

nextset4=[]

for i in range(len(nextset3)):
	(a,b,c,d,e,f)=nextset3[i]
	tmp=[]
	mysettmp=set()
	tmp.append(a)
	tmpset=get_adjoining_set(myset2, tmp)
	if len(tmpset)>0:
		for j in range(len(tmpset)):
			(g,h)=tmpset[j]
			mysettmp=set(h)
			mysettmp=mysettmp.union(set(g))
			mysettmp=mysettmp.union(set(a))
			mysettmp=mysettmp.union(set(b))
			mysettmp=mysettmp.union(set(c))
			mysettmp=mysettmp.union(set(d))
			mysettmp=mysettmp.union(set(e))
			mysettmp=mysettmp.union(set(f))
			if len(mysettmp)==9:
				nextset4.append((g,a,b,c,d,e,f))

print "final ans"
print nextset4


## ans:

#4160357289
#1460357289
#4106357289
#1406357289
#4130952867
#1430952867
#
#sum total = 16695334890
