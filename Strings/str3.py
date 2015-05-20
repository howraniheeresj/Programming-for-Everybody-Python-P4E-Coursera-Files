data = 'From iurihondaf@gmail.com '
atpos = data.find('@')
#print atpos

sppos = data.find(' ', atpos)
#print sppos

host = data[atpos+1 : sppos]
print host