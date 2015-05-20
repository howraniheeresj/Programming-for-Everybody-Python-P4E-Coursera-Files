s = raw_input("Shutdown? ")

def shut_down(s):
    if s == "yes":
        return "Shutting down"
        
    elif s == "not":
        return "Shutdown aborted"
        
    else:
        return "Sorry"
        
shut_down(s)