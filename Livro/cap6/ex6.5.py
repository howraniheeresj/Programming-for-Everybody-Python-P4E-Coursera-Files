str = 'X-DSPAM-Confidence: 0.8475'

num = str.find(":")

number = str[num+2:]
number = float(number)
print number