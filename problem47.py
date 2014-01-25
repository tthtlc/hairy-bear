
## problem 48
import math
import sys

def erasthotene_cross(array, n):
	array = [0 for x in range(n)]
	for i in range(2,n,1):
		if (array[i]==0):
			for j in range(2*i, n, i):
				array[j]=1
	return array

def generate_prime(max_nos):
	array = [0 for x in range(max_nos)]
	array=erasthotene_cross(array, max_nos)
	###array2 = array[:]
	prime_nos=[]
	for i in range(2,max_nos,1):
		if (array[i]!=1):
			prime_nos.append(i)
	return prime_nos

def find_prime_factor(a):
	global prime_factor
	factor=[]
	for i in range(len(prime_factor)):
		if (a%prime_factor[i])==0:
			factor.append(prime_factor[i])
	return factor

total_nos=4
prev_nos_match=False
count=0
max_number=1000000
prime_factor=generate_prime(max_number)
start_number=210 ### 2*3*5*7

for j in range(start_number, max_number):
	next=len(find_prime_factor(j))
	if (next==total_nos):
		if not(prev_nos_match):
			count=0
		prev_nos_match=True
		count+=1
		#print find_prime_factor(j),count
		if (count==4):	
			print j, j-1, j-2, j-3
			print find_prime_factor(j)
			print find_prime_factor(j-1)
			print find_prime_factor(j-2)
			print find_prime_factor(j-3)
	else:
		prev_nos_match=False
		count=0
