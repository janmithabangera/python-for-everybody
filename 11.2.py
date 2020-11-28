import re
handle = open("actual-data.txt")
counts=list()
for line in handle:
    line=line.rstrip()
    x= re.findall('([0-9]+)',line)
    counts=x+counts
sum=0
for z in counts:
    sum = sum + int(z)

print(sum)
 #OR
 import re
print sum([int(i) for i in re.findall('[0-9]+',open(raw_input('Enter The File Name'),'r').read())])
