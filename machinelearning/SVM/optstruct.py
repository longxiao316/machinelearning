import numpy as np
class optStruct:
    def __init__(self,datamatin,classlabels,c,toler):
        self.x=datamatin
        self.labelmat=classlabels
        self.c=c
        self.tol=toler
        self.m=np.shape(datamatin)[0]
        self.alphas=np.mat(np.zeros(self.m,1))
        self.b=0
        self.ecache=np.mat(np.zeros(self.m,2))
def calcEk(os,k):
    fxk=float(np.multiply(os.aphas,os.labelmat).T*(os.x*os.x[k,:].T))+os.b
    ek=fxk-float(os.labelmat[k])
    return ek
def selectJ(i,os,ei):
    maxk=-1
    maxdeltae=0
    ej=0
    os.ecache[i]=[1,ei]
    validecachelist=np.nonzero(os.ecache[:,0].A)
    if (len(validecachelist))>1:
        for k in validecachelist:
            if k==i:
                continue
            ek =calcEk(os,k)
            deltae=abs(ei-ek)
            if(deltae>maxdeltae):
                maxk=k
                maxdeltae=deltae
                ej=ek
        return maxk,ej
    else:
        j=selectJ(i,os.m)
        ej=calcEk(os,j)
def updateEk(os,k):
    ek=calcEk(os,k)
    os.ecache[k]=[1,ek]
a=np.mat("1,2,3;0,1,2;0,3,4")
b=np.mat("0,0,1;0,0,1")
print b
print b.A
print a.A