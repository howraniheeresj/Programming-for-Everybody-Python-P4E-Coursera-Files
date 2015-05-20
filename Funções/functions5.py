phrase = raw_input("Say something please!   ")

def shout(phrase):
    if phrase == phrase.upper():
        print "YOU ARE SHOUTING"
    else:
        print "Can you speak up?"
    
shout(phrase)