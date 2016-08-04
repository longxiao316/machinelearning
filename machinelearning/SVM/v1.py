import random
import numpy as np
def loadDataSet(filename):
    datamat=[];labelmat=[]
    fr=open(filename)
    for line in fr.readlines():
        linearr=line.strip().split('\t')
        datamat.append([float(linearr[0]),float(linearr[1])])
        labelmat.append(float[linearr[2]])
    return datamat,labelmat
def selectJrand(i,m):
    j=i
    while(j==i):
        j=int(random.uniform(0,m))
    return j
def clipAlpha(aj,h,l):
    if aj>h:
        aj=h
    if l>aj:
        aj=l
    return aj
def smosimple(datamatin,classlabels,c,toler,maxiter):
    datamat=np.mat(datamatin);labelmat=np.mat(classlabels).transpose()
    b=0
    m,n=np.shape(datamat)
    alphas=np.mat(np.zeros((m,1)))
    iter=0
    while(iter<maxiter):
        alphapairschanged=0
        for i in range(m):
            fxi=float(np.multiply(alphas,labelmat)).T*(datamat*datamat[i,:].T)+b
            ei=fxi-float(labelmat[i])
            if ((labelmat[i]*ei<-toler)  and (alphas[i]<c)) or ((labelmat[i]*ei>toler) and (alphas[i]>0)):
                j=selectJrand(i,m)
                fxj=float(np.multiply(alphas,labelmat).T*(datamat*datamat[j:].T))+b
                ej=fxj-float(labelmat[j])
                alphaiold=alphas[i].copy()
                alphajold=alphas[j].copy()
                if(labelmat[i]!=labelmat[j]):
                    L=np.max(0,alphas[j]-alphas[i])
                    H=min(c,c+alphas[j]-alphas[i])
                else:
                    L=max(0,alphas[j]+alphas[i]-c)
                    H=min(c,alphas[j]+alphas[i])
                if L==H: print "L==H"; continue
                eta=2.0*datamat[i,:]*datamat[j,:].T-datamat[i,:]*datamat[i,:].T-datamat[j,:]*datamat[j,:].T
                if eta>=0: print "eta>0"; continue;
                alphas[j]-=labelmat[j]*(ei-ej)/eta
                alphas[j]=clipAlpha(alphas[j],H,L)
                if(abs(alphas[j]-alphajold)<0.00001):
                    print "j is not moving enough "
                    continue
                alphas[i]+=labelmat[j]*labelmat[i]*(alphajold-alphas[j])
                b1=b-ei-labelmat[i]*(alphas[i]-alphaiold)*datamat[i,:]*datamat[i,:].T-labelmat[j]*(alphas[j]-alphajold)*datamat[i,:]*datamat[j,:].T
                b2=b-ej-labelmat[i]*(alphas[i]-alphaiold)*datamat[i,:]*datamat[j,:].T-labelmat[j]*(alphas[j]-alphajold)*datamat[j,:]*datamat[j,:].T
                if (0<alphas[i]) and (c>alphas[i]):
                    b=b1
                elif (0<alphas[j]) and (c>alphas[j]):
                    b=b2
                else:
                    b=(b1+b2)/2.0
                alphapairschanged+=1
                print "iter:%d i:%d ,pairs changed %d" % (iter,i,alphapairschanged)
                if(alphapairschanged==0):
                    iter+=1
                else:
                    iter=0
                print "iteration number :%d" % iter
            return b,alphas
    

