import math
from cmath import phase

com = input()
operator=com.rfind('+')
if(operator==-1):
    operator = com.rfind('-')
real = com[0:operator]
imaginary = com[operator:]
imaginary = imaginary[0:-1]
dist = float(real) * float(real) + float(imaginary) * float(imaginary)
dist = math.sqrt(dist)
print(dist)
print(phase(complex(float(real), float(imaginary))))





# -1-5j
# 5.09901951359
# -1.76819188664

from cmath import polar

#
# com = input()
#
# compl = complex(com)
#
# print(compl)
# print(phase(compl))
# print(polar(compl))

