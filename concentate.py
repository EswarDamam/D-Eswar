import numpy
A,B, C= map(int, raw_input().split())
X = numpy.array([map(int, raw_input().split()) for x in range(A)])
Y = numpy.array([map(int, raw_input().split()) for x in range(B)])
print numpy.concatenate((X,Y),axis=0)