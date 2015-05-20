hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

h = int(hours)
r = int(rate)

if h <=40:
    pay = h*r
else:
    pay = (40*r) + (1.5*r*(h-40))

p = float(pay)

print "Pay", p