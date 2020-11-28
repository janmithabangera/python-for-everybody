def computepay(h,r):
    if h>40:
        p=1.5*r*(h-40)+(40*r)#definition of the program pay rate for up to 40 hours is suppose x and above 40 hours is 1.5x .
        # Divide this equation in 2 part 1st is (40 r) which compute the pay of 40 hours.
        # 2nd part is 1.5 * r * (h - 40) which computes the pay for hours > 40.
        #here h is 45 so divide in 40 + 5. for 40 hours pay rate is x and for 5 hours pay rate is 1.5x.
        #total pay rate is payrate(40 hours) +payrate(hour>40) .
        # so compute the 1st part 4010.50= 420 now compute 2nd part (45-40) 1.510.50 = 51.510.50=78.75 .
        # now add 1st part and second part 420+78.75=498.75.try is for 52 hours . 1st part 4010.50=420 and 2nd part (52-40)1.510.50=121.510.50=189.
        # s0 answes is 1st part+ 2nd part = 420+189=609. try this value on your code
    else:
        p=h*r
    return p
hrs = input("Enter Hours:")
rate =input("enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
