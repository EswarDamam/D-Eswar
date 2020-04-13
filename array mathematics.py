import numpy

X, Y = map(int, input().split())

C = numpy.array([list(map(int, input().split())) for n in range(N)])
D = numpy.array([list(map(int, input().split())) for n in range(N)])

print (C + D)
print (C - D)
print (C * D)
print (C // D)
print (C % D)
print (C ** D)