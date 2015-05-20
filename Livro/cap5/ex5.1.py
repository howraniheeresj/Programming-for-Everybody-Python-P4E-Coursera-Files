total = 0
count = 0

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
        
        average = float(total)/float(count)
        
    except:
        print 'bad data'
        continue
        
print 'Total, count and average: ', total, count, average