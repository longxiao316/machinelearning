#coding:utf-8
import sys
import os
import sklearn.datasets.base as bs
import cPickle as pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

reload(sys)
sys.setdefaultencoding('gb18030')

def readbunchobj(path):
    fileobj = open(path,"rb")
    bunch=pickle.load(fileobj)
    fileobj.close()
    return bunch
def writebunchobj(path,bunchobj):
    fileobj = open(path,"wb")
    pickle.dump(bunchobj,fileobj)
    fileobj.close()
path=""
bunch=readbunchobj(path)
