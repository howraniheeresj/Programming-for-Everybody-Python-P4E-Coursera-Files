
#table = [["Score", "Grade"],[">= 0.9", "A"], [">= 0.8", "B"], [">= 0.7", "C"], [">= 0.6", "D"], ["< 0.6", "F"]]

while True:
    score_prompt = raw_input("Enter score: ") 
    try:
        score = float(score_prompt)
        if score >= 0.0 and score <= 1.0:
            if score >= 0.9:
                print "Grade A"
                break
            elif score >= 0.8:
                print "Grade B"
                break
            elif score >= 0.7:
                print "Grade C"
                break
            elif score >= 0.6:
                print "Grade D"
                break
            elif score < 0.6:
                print "Grade F"
                break
                
        else:
            print "This is not a valid score"
            continue
        
    except:
        print "This is not a valid score"
        continue