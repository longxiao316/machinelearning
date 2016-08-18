import numpy as np


class NBayes():
    def __init__(self):
        self.vocabulary=[]
        self.labels=[]
        self.tf=0
        self.idf=0
        self.df=0
        self.cp=0 #p(xi|yi)
        self.labelEvidence={} #p(yi)
        self.labelcount=0
        self.vocabularyLen = 0
        self.docLen=0
        self.testSet=0
    def cal_label(self,lables):
        self.labels = set(lables)
        self.docLen=len(lables)
        for label in self.labels:
            count = lables.count(label)
            self.labelEvidence[label]=float(count)/float(self.docLen)
    def train(self,data):
        #calculate all labels and p(yi)
        self.cal_label(data[:,-1])
        self.cal_wordFreq(data)
    def cal_wordFreq(self,data):
        self.tf=[self.docLen,self.vocabularyLen]
        self.df=[self.vocabularyLen]

        for d in range(self.docLen):
            doc=data[d]
            for i in range(self.vocabularyLen):
                term=self.vocabulary[i]
                count=doc.count(term)
                self.tf[d,i]=count
    def cal_cp(self):
        self.cp=[self.labelcount,self.vocabularyLen]
        return
    def classify(self):
        return
a= np.arange(16).reshape(4,4)
print a
print '---------------'
print a[:,-1]