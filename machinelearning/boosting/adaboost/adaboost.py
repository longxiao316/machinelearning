import numpy as np
def stumpclassify(datamat,dimen,threshold,inequality):
    retarr=np.ones((np.shape(datamat)[0],1))
    if(inequality=='lt'):
        print retarr[datamat[:, dimen] <= threshold]
        retarr[datamat[:,dimen]<=threshold]=-1#this usage of array is not quite understandable
    else:
        retarr[datamat[:,dimen]>threshold]=-1
    return retarr
