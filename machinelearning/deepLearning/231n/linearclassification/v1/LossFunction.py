# -*- coding:utf-8 -*-
import numpy as np
#svm loss without regularization:
def L_i(x,y,w):
    """
    unvectorized version, compute the multiclass svm loss for a single example(x,y)
    -----x is a column vector representing an image(e.g. 3073*1 in cifar-10),
        with an appended bias dimension in the 3073-rd position (i.e. bias trick)
    -----y is an integer giving index of correct class
    -----w is the weight matrix
    """
    delta=1.0 #svm中的间隔
    scores=w.dot(x)
    correct_class_score=scores[y]


