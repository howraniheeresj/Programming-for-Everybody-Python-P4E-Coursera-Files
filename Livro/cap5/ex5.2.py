total = 0
count = 0
smallest = None
largest = None

lst = []

while True:
    number = raw_input('Insert a number here (say when you are done): ')
    if number == 'done': break
    print number
    
    try:
        number = int(number)
        lst.append(number)
        
        total = total + number
        
        count = count + 1
        
    except:
        print 'bad data'
        continue
        

for number in lst:
    if smallest is None or number < smallest:
        smallest = number
        
for number in lst:
    if largest is None or number > largest:
        largest = number

print total, count, smallest, largest