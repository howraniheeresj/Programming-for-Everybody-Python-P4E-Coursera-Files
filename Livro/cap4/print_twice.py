import math
from math import pi

def print_twice(bruce):
    print bruce
    print bruce
    
print_twice('Spam')
print_twice(17)
print_twice(math.pi)
print_twice('Spam '*4)
print_twice(math.cos(math.pi))

result = print_twice('Bing')
print result