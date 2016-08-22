import numpy as np
def t1():
    m=np.array([[range(2),range(2)]])
    print m
    print m.shape
    return m
def t2():
    b=np.arange(5)
    print b.dtype.itemsize
    return
def t3():
    a=np.arange(9).reshape(3,3)
    b=np.arange(5,14).reshape(3,3)
    print a
    print b
    print np.concatenate(a,b)
t3()