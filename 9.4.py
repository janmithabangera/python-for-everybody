fname = input("Enter file name: ")#mbox-short.txt
if len(name) < 1 : name = "mbox-short.txt"
handle= open(fname)
counts=dict()
for line in handle:
    line=line.rstrip()
    if not 'From:' in line:
        continue
    words = line.split()
    word=words[1]
    counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for words,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)
