def tax(bill):
    bill *= 1.08
    print "With tax: %f" % bill
    return bill
    
def tip(bill):
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    

meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
meal_cost = 100