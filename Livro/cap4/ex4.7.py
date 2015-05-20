score = 0

def computegrade(score):
    while True:
        try:
            score = raw_input("Enter a score between 0.0 and 1.0: ")
            score = float(score)
        except: 
            print "Bad score"  
            continue 
         
        if score >= 0.0 and score <= 1.0:
            if score > 0.9:
                grade = "A"
            elif score > 0.8:
                grade = "B"
            elif score > 0.7:
                grade = "C"
            elif score > 0.6:
                grade = "D"
            else:
                grade = "F"  
            print grade
        else:
            print "Choose a valid number!"
        
computegrade(score)