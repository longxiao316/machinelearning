# -*- coding: utf-8 -*-
import numpy as np

class ID3v4(object):
    def __init__(self):
        self.tree={}
    def loadData(self,data,labels):
        self.data=data
    def maxclass(self,data):
        vals=set(data)
        maxcount=0
        tag=-1
        for v in vals:
            count=vals.count(v)
            if(count>maxcount):
                maxcount=count
                tag=v
        return tag
    def tree_growth(self,dataset,features):
        '''
        递归生成一层子树
        '''
        #如果数据都为同一类，就不需要再分了
        classlist=dataset[:,-1]
        if(classlist.tolist().count(classlist[0])==len(classlist)):
            return classlist[0]
        #如果没有特征了，那就选类数量最大的为最终类
        if(len(dataset[0])==1):
            return  self.maxclass(classlist)
        tree={}
        #选择最好的分类特征
        feat=self.findbestfeature(dataset)
        featclass=features[feat]
        tree[featclass]={}
        del(features[feat])
        #下面根据特征切树
        #特征的值空间
        featvals=set(dataset[:,feat])
        for val in featvals:
            subdataset=self.splitdataset(dataset,feat,val)
            tree[featclass][val]=self.tree_growth(np.array(subdataset),features)
        return tree
    def findbestfeature(self,dataset):
        #划分前的熵
        baseentropy=self.cal_entropy_onattribute(dataset,-1)
        #最大信息增益
        maxinfgain=0.0
        #最优特征
        bestfeat=-1
        #下面算划分后的熵
        featurecount=len(dataset[0])-1
        if(featurecount<=0):
            return -1
        for i in range(featurecount):
            #把数据按当前特征的值划分，并算熵
            curfeat=dataset[:,i]
            distinctfeat=set(curfeat)
            #当前信息增益
            curig=0.0
            curentropy=0.0
            for f in distinctfeat:
                prob = float(curfeat.tolist().count(f))/float(len(curfeat))
                subdataset=self.splitdataset(dataset,i,f)
                curentropy+=prob*self.cal_entropy_onattribute(np.array(subdataset),-1)
            curig=baseentropy-curentropy
            if(curig>maxinfgain):
                maxinfgain=curig
                bestfeat=i

        return bestfeat

    def splitdataset(self,dataset,feat,val):
        '''
        选出dataset中特征feat值为val的行，并删除feat所在列
        '''
        subdata=[]
        for line in dataset:
            if(line[feat]==val):
                reduceline=line[:feat]
                reduceline=np.append(reduceline,line[feat+1:])
                subdata.append(reduceline)
        return subdata
    def cal_entropy_onattribute(self,samples,i):
        '''
        计算sample（matrix）在第i列特征上的熵
        '''
        labels=samples[:,i]
        probs=[]
        for l in set(labels):
            probs.append(float(labels.tolist().count(l))/len(labels))
        return -np.sum(probs*np.log(probs))
    def predict(self,tree,data):
        while(isinstance(tree,dict)):
            feat=tree.keys()[0]
            subtree=tree[feat]
            tree=subtree.get(np.str(data[feat]))
        return tree

def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    features = ['no surfacing','flippers']
    return dataSet,features
if __name__ == '__main__':
     m=ID3v4()
     dataset,features = createDataSet()
     tree = m.tree_growth(np.array(dataset),features)
     print tree
     print m.predict(tree,{'no surfacing':1,'flippers':1})
     print m.predict(tree,{'no surfacing':1,'flippers':0})
     print m.predict(tree,{'no surfacing':0,'flippers':1})
     print m.predict(tree,{'no surfacing':0,'flippers':0})


