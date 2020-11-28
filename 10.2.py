name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    line= line.split()
    line=line[5]
    line=line[0:2]
    counts[line]=counts.get(line,0)+1
#print(counts)
lst=list()
for value,count in sorted(counts.items()):
    lst.append((value,count))
for value,count in lst:
    print(value,count)
