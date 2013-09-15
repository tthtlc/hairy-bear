
import numpy as np
data = np.genfromtxt("/tmp/words.txt",delimiter="\n")
mylen=len(data)

for i in range(mylen):
	s = data[i]
	print s
#[ord(c) for c in s]
#[104, 105]


