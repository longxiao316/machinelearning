import numpy as np
a=np.arange(12).reshape(3,4)
print a
b=np.nonzero(a[:,1]>2)
print np.shape(a)
print b
# print b[0]
print a[b[0],:][0]

