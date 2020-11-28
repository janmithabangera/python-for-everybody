hrs=input("enter the hours")
rate=input("enter the rate")
try:
    h=float(hrs)
    r=float(rate)
except:
    print('error,please enter numeric input')
    quit() #coz u dont want it to show the trace back error
print(h,r)
if h>40:
    rep=h*r
    otp=(h-40)*(r*0.5) #this is to calculate the extra pay for more 40hrs
    xp=rep+otp
else:
    xp=h*r
print(xp)
