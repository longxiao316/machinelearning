import numpy as np

a= np.arange(5)
b=np.arange(3,6)
print a
print b
k= np.meshgrid(a,b)
print k[0]
print
print k[1]
print "-----------"
k=np.meshgrid(b,a)
print k[0]
print
print k[1]