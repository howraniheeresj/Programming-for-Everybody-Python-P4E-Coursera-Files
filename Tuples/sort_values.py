# coding=utf-8

c = {'a': 10, 'b': 1, 'c': 22}
#o objetivo é agora organizar não por key, mas por value, por exemplo, a organização não é feita pelo 'a', mas pelo 10

tmp = list()
for k,v in c.items():
    tmp.append( (v,k) )
    
print tmp

tmp.sort(reverse=True)
#sort from the highest to the lowest

print tmp