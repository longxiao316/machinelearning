import numpy as np
import matplotlib.pyplot as plt
import random

def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr=open("testset.txt")
    for line in fr.readlines():
        linearr=line.strip().split()
        dataMat.append([1.0,float(linearr[0]),float(linearr[1])])
        labelMat.append(int(linearr[2]))
    return dataMat,labelMat
def sigmod(inx):
    return 1.0/(1+np.exp(-inx))
def gradAscent(datamatin,classlabels):
    datamatrix=np.mat(datamatin)
    labelmat=np.mat(classlabels).transpose()
    m,n=np.shape(datamatrix)
    alpha=0.001
    maxcycles=500
    weights=np.ones(n,1)
    for k in range(maxcycles):
        h=sigmod(datamatrix*weights)
        error=(labelmat-h)
        weights=weights+alpha*datamatrix.transpose()*error
    return weights
def plotBestFit(wei):
    weights=wei.getA()
    datamat,labelmat=loadDataSet()
    dataarr=np.array(datamat)
    n=np.shape(dataarr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelmat[i])==1 :
            xcord1.append(dataarr[i,1]);ycord1.append(dataarr[i,2])
        else:
            xcord2.append(dataarr[i,1]);ycord2.append(dataarr[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=np.arange(-3.0,3.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1');plt.ylabel('X2')
    plt.show()
def stoGradAacent0(datamat,classlabels):
    m,n=np.shape(datamat)
    alpha=0.01
    weights=np.ones(n)
    for i in range(m):
        h=sigmod(datamat[i]*weights)
        error=classlabels[i]-h
        weights=weights+alpha*error*datamat[i]
    return weights
def stoGradAscent1(datamat,classlabel,numiter=150):
    m,n=np.shape(datamat)
    weights=np.ones(n)
    for j in range(numiter):
        dataindex=range(m)
        for i in range(m):
            alpha=4/(1.0+j+i)+0.01
            randindex=int(random.uniform(0,len(dataindex)))
            h=sigmod(sum(datamat[randindex]*weights))
            error=classlabel[randindex]-h
            weights=weights+alpha*error*datamat[randindex]
            del(dataindex[randindex])
    return weights
def classifyVector(inx,weights):
    prob=sigmod(sum(inx*weights))
    if prob>0.5: return 1.0
    else: return 0.0
def colicTest():
    frtrain=open("horsecolicTraining.txt")
    frtest=open('horsecolictest.txt')
    trainingSet=[];traininglabels=[]
    for line in frtrain.readlines():
        currline=line.strip().split('\t')
        linearr=[]
        for i in range(21):
            linearr.append(float(currline[i]))
        trainingSet.append(linearr)
        traininglabels.append(float(currline[21]))
    trainweights=stoGradAscent1(np.array(trainingSet),traininglabels,500)
    errorcount=0;numtestvec=0.0
    for line in frtest.readlines():
        numtestvec+=1.0
        currline=line.strip().split('\t')
        linearr=[]
        for i in range(21):
            linearr.append(float(currline[i]))
        if int(classifyVector(np.array(linearr),trainweights)) != int(currline[21]):
            errorcount+=1
    errorRate=(float(errorcount)/numtestvec)
    print 'the error rate  of this test is : %f' % errorRate
    return errorRate
def multitest():
    numTests=10;errorSum=0.0
    for k in range(numTests):
        errorSum+=colicTest()
    print "after %d iterations the average error rate is : %f" % (numTests,errorSum/float(numTests))
    


