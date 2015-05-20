largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    
    if num == "done" : break
    
    try:
        number = int(num)
    except:
        print "Invalid input"
        continue


    if number > largest:
        largest = number
    
    if number < smallest:   
        smallest = number
            
print "Maximum is", largest
print "Minimum is", smallest