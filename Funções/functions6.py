num = raw_input("Type a number: ")
number = int(num)

def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        print cube(number)
        
    else:
        print "PEEEEE"
        
by_three(number)