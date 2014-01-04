#   to answer problem 17:   
#### python problem17.py | sed 's/ //g'| wc
####    1000    1000   22124
#### subtracting all the newlines from each line above give the exact answer


import math

i=1
sum_square=0

sum=0

number_word=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
i_max=9

number_word2=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
i2_max = 10

number_word1=["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
i1_max=8

i=0
while i < i_max:
    	print number_word[i]
	i+=1
i=0
while i < i2_max:
    	print number_word2[i]
	i+=1
i=0
while i < i1_max:
	j=0
    	print number_word1[i]
	while j < i_max:
    		print number_word1[i]+" "+number_word[j]
		j+=1
	i+=1

h=0
while h < i_max:
	### x hundred
	print number_word[h]+" "+"hundred" 
	i=0
	### x01-x10
	while i < i_max:
	    	print number_word[h]+" "+"hundred" + " "+"and"+" "+ number_word[i]
		i+=1
	
	
	### x11-x19
	i2=0
	while i2 < i2_max:
	    	print number_word[h]+" "+"hundred" + " "+"and"+" "+ number_word2[i2]
		i2+=1
	
	### x20-x99
	i1=0
	while i1 < i1_max:
	    	print number_word[h]+" "+"hundred" + " and "+ number_word1[i1]
	#    	s1=number_word[i]+" "+"hundred" + " "+"and"+" "+ number_word1[i1]
		i=0
		while i < i_max:
	    		print number_word[h]+" "+"hundred" + " "+"and"+" "+ number_word1[i1]+" " + number_word[i]
			i+=1
		i1+=1
	h+=1

print number_word[0]+" "+"thousand"
