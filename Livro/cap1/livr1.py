prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = raw_input(prompt)

try:
    speed2 = int(speed)
    print speed2
    
except:
    speed2 = -1
    print "This is not a number"