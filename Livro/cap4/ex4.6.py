hours = raw_input("Enter Hours: ")
try:
    h = float(hours)
except:
    print "This is not a valid number"

rate = raw_input ("Enter Rate: ")
try:
    r = float(rate)
except:
    print "This is not a valid number"
    
def computepay(h,r):

    if h <= 40:
        return h*r
    else:
        return 40*r + (1.5*r*(h-40))
    
print "Pay:", computepay(h,r)