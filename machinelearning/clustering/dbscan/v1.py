import numpy as np
import matplotlib.pyplot as plt
import random
import collections

# s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# d=collections.defaultdict(lambda :[[],[]])
# for k,v in s:
#     d[k].append(v)
# print d['yellow'][2]
# print list(d.items())
visited=[]
abnormal=[]
classified=[]

def isclassified(d):
    return True
def markclassified(d):
    return
def isvisited(d):
    return True
def markvisited(d):
    return True
def distance(a,b):
    return np.sum(np.square(a-b))
def neighbors(p,data,e):
    nbs = []
    for d in data:
        if p[0]-d[0] < e:
            if distance(p,d)<e:
                nbs.append(d)
    return nbs

def expand(d,data,e,minnb,c):
    c.append(d)
    neighbor=neighbors(d,data,e)
    for n in neighbor:
        subn=neighbors(n,data,e)
        if len(subn) > minnb:
            expand(n,data,e,minnb,c)
        if not isclassified(n):
            c.append(n)
            markclassified(n)
    if len(neighbor)>minnb:
        for n in neighbor:
            if not isvisited(n):
                expand(n,data,e,minnb,c)
            else:
                c.append(n)
            markvisited(n)
    else:
        for n in neighbor:
            c.append(n)
            markvisited(n)
    return c
def markabnormal(d):
    return
def randcolor():
    return (random.random(),random.random(),random.random())
def cluster(data,e,minnb):
    cs={}
    count=0
    for d in data:
        if isvisited(d):
            continue
        # markvisited(d)
        markvisited(d)
        nbs =  neighbors(d,data,e)
        if len(nbs) > minnb:
            #we can get one classification c through this expand
            count+=1
            c=[]
            expand(d,data,e,minnb,c)
            cs[count]=c
        else:
            markabnormal(d)
    return
dt=[random.random()*100000 for i in range(10000)]
data=np.array(dt).reshape(5000,2)
mtxs=cluster(data,1,10)
for m in mtxs:
    mtx=np.array(m)
    if mtx.size > 0:
        plt.scatter(mtx[:,0],mtx[:,1],color=randcolor())
plt.show()