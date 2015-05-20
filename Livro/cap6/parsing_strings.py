data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

mail = data.find('@')
print mail

space = data.find(' ', mail)
print space

host = data[mail+1:space]

print "The host: ", host

print ' '

date = data[space+1:]
print "The date: ", date