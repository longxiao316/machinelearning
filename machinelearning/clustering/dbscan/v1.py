import numpy as np
import matplotlib.pyplot as plt
import collections

# s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# d=collections.defaultdict(lambda :[[],[]])
# for k,v in s:
#     d[k].append(v)
# print d['yellow'][2]
# print list(d.items())
visited=[]
abnormal=[]


def isvisited(d):
    return True
def markvisited(d):
    return True
def distance(a,b):
    return
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
    if len(neighbor)>minnb:
        for n in neighbor:
            if not visited.__contains__(n):
                expand(n,data,e,minnb,c)
            else:
                c.append(n)
    else:
        for n in neighbor:
            c.append(n)
    return c
def markabnormal(d):
    return

def cluster(data,e,minnb):
    cs={}
    count=0
    for d in data:
        if visited.__contains__(d):
            continue
        # markvisited(d)
        visited.append(d)
        neighbours =  neighbors(d,data,e)
        if len(neighbors) > minnb:
            #we can get one classification c through this expand
            count+=1
            c=[]
            expand(d,data,e,minnb,c)
            cs[count]=c
        else:
            # markabnormal(d)
            abnormal.append(d)
    return

