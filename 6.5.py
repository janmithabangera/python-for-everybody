text = "X-DSPAM-Confidence:    0.8475";
num= text.find(':')
print(num)
sppos=text.find('    ')
print(sppos)
fsppos=float(sppos)
pos=text[sppos+4:]
print(pos)
