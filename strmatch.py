
import re
line = 'This,is,a,sample,string'
line = ' sample,string'
print re.match("sample", line)

print re.search("sample", line)
