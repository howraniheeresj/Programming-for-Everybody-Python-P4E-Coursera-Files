while True:
    num = raw_input("Choose a number between 0 and 10: ")
    
    try:
        number = float(num)
        if number >= 0 and number <= 10:
            print number
            break
        else:
            print "The number must have a value between 0 and 10"
            continue
    
    except:
        print "Choose a valid number"
        continue