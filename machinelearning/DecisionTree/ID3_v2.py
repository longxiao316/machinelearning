import numpy as np

class ID3V2(object):
    def __init__(self):
        self.data=[]
        self.model={}
        self.labels=[]
        return
    def loadData(self,data):

        self.data=data
        return
    def train(self):
        self.labels=set(self.data[:,-1])
        featurecount = np.shape(self.data)[1]
        for i in range(featurecount-1):#the last column is tag
            pass
        traindata=self.data
        return
    def predict(self,x):
        return
    def cal_entropy_onattribute(self,samples,i):
        labels=samples[:,i]
        probs=[]
        for l in set(labels):
            probs.append(float(labels.tolist().count(l))/len(labels))
        return -np.sum(probs*np.log(probs))
    def cal_informationGain_onattribute(self,i):
        #we will calculate the information gain :
        # G(D,A)=H(D)-H(D|A)=-sum(p(Di)*ln(p(Di)) - (-sum_i(sum_j(p(Aj)p(Di|Aj)*ln(p(Di|Aj))))
        #
        #first calculate H(D)
        h_d=self.cal_entropy_onattribute(-1)


        return 0

a=ID3V2()
a.loadData(5)
d=np.arange(12).reshape(3,4)
print d
print np.shape(d)[1]