count = 0
sum = 0
print 'Before', count, sum

for value in [12, 123, 31231, 15435, 5, 65, 245, 4]:
    count = count + 1
    sum = sum + value
    print count, sum, value
    
print 'After', count, sum, sum/count