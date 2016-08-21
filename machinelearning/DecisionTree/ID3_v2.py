import numpy as np

class ID3V2(object):
    def __init__(self):
        self.data=[]
        return
    def loadData(self,data):

        self.data=data
        return
    def train(self):
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
        #first calculate H(D)
        h_d=self.cal_entropy_onattribute(-1)

        return 0

a=ID3V2()
a.loadData(5)
a.train()
d=np.arange(9).reshape(3,3)
print a.cal_entropy_onattribute(d,-1)