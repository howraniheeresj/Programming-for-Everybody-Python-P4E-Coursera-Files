zork = 0
print 'Before', zork
for thing in [12, 123, 31231, 15435, 5, 65, 245, 4]:
    zork = zork + 1
    print zork, thing
    
print 'After', zork


print 'Before', zork
for thing in [12, 123, 31231, 15435, 5, 65, 245, 4]:
    zork = zork + thing
    print zork, thing
    
print 'After', zork