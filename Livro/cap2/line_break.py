name = raw_input('What is your name?\n')
print name

prompt = 'Tell me your number\n'
num = raw_input(prompt)
try:
    number = int(num)
    print "Your number * 5 is: ", int(number)*5
    
except:
    print "Not a number"