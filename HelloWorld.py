from numpy import *

print "Hello World, Python And Machine Learning!"

arrayRand = random.rand(4, 4)
print arrayRand

matRand = mat(arrayRand)
print matRand

invMatRand = matRand.I
print invMatRand

print matRand * invMatRand

print matRand * invMatRand - eye(4)

