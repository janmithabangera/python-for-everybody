# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
f=fh.read()
print(f[0:].upper().rstrip())

#or
for line in fh:
    f=line.rstrip()
    print(f.upper())
