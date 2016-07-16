import numpy as np
import random
import matplotlib.pyplot as plt
def randcenter(data,k):
    #for simplicity ,just pick up random points
    ct=[data[random.randint(0,k-1)] for i in range(k)]
    return ct
def randcolor():
    return (random.random(),random.random(),random.random())
def calcenter(data):
    ct=[]
    for d in data:
        if len(d)>0:
            ct.append(np.sum(d,axis=0)/len(d))
    return  ct
def distance(v1,v2):
    return np.sum(np.square(v1-v2))

def cluster(data,k):
    ct=randcenter(data,k)
    for i in range(10):
        if(i>0):
            nct=calcenter(clst)
            k=len(nct)
            ct=nct
        clst=[[] for i in range(k)]
        for v in data:
            idx=0
            dist=-1
            for j in range(k):
                c=ct[j]
                d=distance(c,v)
                if(d<dist or dist<0):
                    dist=d
                    idx=j
            clst[idx].append(v)
    return clst
dt=[random.random()*100000 for i in range(10000)]
data=np.array(dt).reshape(5000,2)
mtxs=cluster(data,5)
for m in mtxs:
    mtx=np.array(m)
    if mtx.size > 0:
        plt.scatter(mtx[:,0],mtx[:,1],color=randcolor())
plt.show()