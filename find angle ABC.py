import cmath
import math
AB = int(raw_input())
BC = int(raw_input())

print str(int(round(math.degrees(cmath.phase(complex(BC,AB)))))) + '°'
