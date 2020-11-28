sum=0
count=0
while True:
    sval=input('enter a number')
    if sval =="done":
        break
    try:
        ival=float(sval)
    except:
        print('invalid input')
    continue
    sum=sum+ival
    count=count+1
try:
    print(sum,count,sum/count)
except:
    print('cannot divide by zero')
