import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegressionCV
np.random.seed(0)
x,y=make_moons(200,noise=0.20)
# print x
# plt.scatter(x[:,0],x[:,1],s=40,c=y,cmap=plt.cm.Spectral)
# plt.show()
def plot_decision_boundary(pred_func):
    x_min,x_max=x[:,0].min()-.5,x[:,0].max()+.5
    y_min,y_max=x[:,1].min()-.5,x[:,1].max()+.5
    h=0.01
    xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

    z=pred_func(np.c_[xx.ravel(),yy.ravel()])
    z=z.reshape(xx.shape)

    plt.contourf(xx,yy,z,cmap=plt.cm.Spectral)
    # plt.scatter(x[:,0],x[:,1],s=40,c=y,cmap=plt.cm.Spectral)
clf=LogisticRegressionCV()
clf.fit(x,y)
plot_decision_boundary(lambda x:clf.predict(x))
plt.title("logistic regression")
plt.show()