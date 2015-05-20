d = {'a': 10, 'b': 1, 'c': 22}
d.items()
t = sorted(d.items())
print t

for k,v in sorted(d.items()):
    print k, v