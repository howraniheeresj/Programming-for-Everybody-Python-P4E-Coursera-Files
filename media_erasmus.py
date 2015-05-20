sua_nota = raw_input("Insira sua nota: ")
sua_not = float(sua_nota)

notas = (11, 15, 11, 11, 9, 11, 8, 19, 8, 12, 13, 17, 13, 13, 9, 17, 14, 12, 8)
total = 0
count = 0
for nota in notas:
    count = count + 1
    total = total + nota
    
def media(total, count):
    media = float(total)/float(count)
    return media
    
print media(total, count)

med = float(media(total,count))

def dif(sua_not, med):
    dif = sua_not - med
    return dif
    
print dif(sua_not, med)


