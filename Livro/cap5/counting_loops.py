count = 0
sum_number = 0
for number in [1, 2, 1, 312, 12, 31, 2, 12, 31, 2, 123, 32, 21]:
    count = count +1
# conta o numero de variaveis
    sum_number = sum_number + number
    med = float(sum_number)/float(count)
print "Quantidade:", count, "Soma:", sum_number, "Media:", med