import numpy as np

def loadDataSet(filename):
    datamat=[]
    fr=open(filename)
    for line in fr.readlines():
        curline=line.strip().split("\t")
        fitline=map(float,curline)
        datamat.append(fitline)
    return datamat
def binSplitDataSet(dataSet,feature,value):
    mat0=dataSet[np.nonzero(dataSet[:,feature]>value)[0],:]
    mat1=dataSet[np.nonzero(dataSet[:,feature]<=value)[0],:]
    return mat0,mat1
def regleaf(dataset):
    return np.mean(dataset[:,-1])
def regErr(dataSet):
    return np.var(dataSet[:,-1])*np.shape(dataSet)[0]
def bestSplitFeature(dataset,leaftype=regleaf,errtype=regErr,ops=(1,4)):
    # 检查是否需要再分,什么情况下不需要再分呢？？1，标签方差小于一定值，2，没有再可分的属性,这个放在选特征这个方法里
    #ops第一个是算方差减小(相当于信息增益)下界，当方差减小值小于这个下界的时候就没有必要再分，第二个是叶子节点最少的元素数目
    minvar=ops[0],minleaf=ops[1]
    #方差为0就没有必要再分了
    if (len(set(dataset[:-1].tolist()[0]))==1):
        return None,leaftype(dataset)
    #每个特征遍历算方差(记得写ID3的时候，分过的特征是会被删掉的，而这里分过的特征没有被删掉，为什么要这样)
    m,n=np.shape(dataset)
    basevar = errtype(dataset)
    bestvar= np.inf
    bestfeat=0
    bestval=0
    #遍历特征
    for f in range(n-1):
        #计算按该特征分割的方差和，选取方差最小的那个
        fvals=set(dataset[:,f])
        curvar=0
        #计算特征的哪个val方差最小
        for fv in fvals:
            l,r=binSplitDataSet(dataset,f,fv)
            if np.shape(l)[0]<minleaf or np.shape(r)[0]<minleaf: continue
            l
            tvar=errtype(l)+errtype(r)
            if(tvar<bestvar):
                bestvar=tvar
                bestfeat=f
                bestval=fv
    if(basevar-bestval<minvar):
        return None,leaftype(dataset)
    return bestfeat,bestval
def buildTree(dataSet,leaftype=regleaf,errtype=regErr,ops=(1,4)):

    #进行分割
    bstfeat,bstval=bestSplitFeature(dataSet)
    if bstfeat==None:return bstval
    tree={}
    tree['spltfeat']=bstfeat
    tree['spltval']=bstval
    left,right=binSplitDataSet(dataSet,bstfeat,bstval)
    tree['left']=buildTree(left,leaftype,errtype,ops)
    tree['right']=buildTree(right,leaftype,errtype,ops)
    return tree
def predict(tree,data):
    while(isinstance(tree,dict)):
        if(data[tree['spltfeat']]<tree['spltval']):
            tree=tree['left']
        else:
            tree=tree['right']
        pass
    return tree
def istree(obj):
    return (type(obj).__name__=='dict')
def getmean(tree):
    if(istree(tree['right'])):tree['right']=getmean(tree['right'])
    if(istree(['left'])):tree['left']=getmean(tree['left'])
    return (tree['left']+tree['right'])/2.0
def prune(tree,testdata):
    return tree
a=np.arange(9).reshape(3,3)
print a
print binSplitDataSet(a,1,2)