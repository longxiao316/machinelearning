import numpy as np
import scipy as spy
def calmean(data):
    mn=np.mean(data,axis=0)
    rs=data-mn
    return rs
'''calculate variance'''
def calvar(data):
    mn=calmean(data)
    v=np.transpose(mn)*mn
    return v
def order(l,u):

    return
def pca(data,p):
    dt=calvar(data)
    print dt
    lda,u=np.linalg.eig(dt)
    ids=np.argsort(lda)
    idscut=ids[p+1:]
    up=u[:idscut]
    return np.matrix(data)*np.matrix(up)
a=np.array([1,2,3,4,5,8,7,8,9]).reshape(3,3)

print a[:,[1,2]]