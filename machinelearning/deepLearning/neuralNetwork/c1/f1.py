import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegressionCV
np.random.seed(0)
x,y=make_moons(200,noise=0.20)

'''-----------------------------------linear regerssion---------------------------------------'''
def plot_decision_boundary(pred_func):
    x_min,x_max=x[:,0].min()-.5,x[:,0].max()+.5
    y_min,y_max=x[:,1].min()-.5,x[:,1].max()+.5
    h=0.01
    xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

    z=pred_func(np.c_[xx.ravel(),yy.ravel()])
    z=z.reshape(xx.shape)

    plt.contourf(xx,yy,z,cmap=plt.cm.Spectral)
    # plt.scatter(x[:,0],x[:,1],s=40,c=y,cmap=plt.cm.Spectral)

# clf=LogisticRegressionCV()
# clf.fit(x,y)
# plot_decision_boundary(lambda x:clf.predict(x))
# plt.title("logistic regression")
# plt.show()
'''------------------------simple neural network-------------------------------------'''
num_examples=len(x)
nn_input_dim=2
nn_output_dim=2

#gradient descent
epsilon=0.01
reg_lambda=0.01

def cal_loss(model):
    w1,b1,w2,b2=model['w1'],model['b1'],model['w2'],model['b2']
    #forward
    z1=x.dot(w1)+b1
    a1=np.tanh(z1)
    z2=a1.dot(w2)+b2
    exp_scores=np.exp(z2)
    probs=exp_scores/np.sum(exp_scores,axis=1,keepdims=True)
    correct_logprobs=-np.log(probs[range(num_examples),y])
    data_loss=np.sum(correct_logprobs)
    return 1./num_examples*data_loss
def build_model(nn_hdim,num_passes=20000,print_loss=False):
    np.random.seed(0)
    w1=np.random.randn(nn_input_dim,nn_hdim)/np.sqrt(nn_input_dim)
    b1=np.zeros((1,nn_hdim))
    w2=np.random.randn(nn_hdim,nn_input_dim)/np.sqrt(nn_hdim)
    b2=np.zeros((1,nn_output_dim))

    model={}

    for i in xrange(0,num_passes):
        z1=x.dot(w1)+b1
        a1=np.tanh(z1)
        z2=a1.dot(w2)+b2
        exp_scores=np.exp(z2)
        probs=exp_scores/np.sum(exp_scores,axis=1,keepdims=True)

        #backpropgation
        delta3=probs
        delta3[range(num_examples),y]-=1
        dw2=(a1.T).dot(delta3)
        db2=np.sum(delta3,axis=0,keepdims=True)
        delta2=delta3.dot(w2.T)*(1-np.power(a1,2))
        dw1=np.dot(x.T,delta2)
        db1=np.sum(delta2,axis=0)

        #regularization
        dw2+=reg_lambda*w2
        dw1+=reg_lambda*w1

        w1+=-epsilon*dw1
        b1+=-epsilon*db1
        w2+=-epsilon*dw2
        b2+=-epsilon*db2

        model={'w1':w1,'b1':b1,'w2':w2,'b2':b2}
        if print_loss and i%1000==0:
            print "loss after iteration %i : %f" %(i,cal_loss(model))
    return model
def predict(model,x):
    w1,b1,w2,b2=model['w1'],model['b1'],model['w2'],model['b2']
    z1=x.dot(w1)+b1
    a1=np.tanh(z1)
    z2=a1.dot(w2)+b2
    exp_scores=np.exp(z2)
    probs=exp_scores/np.sum(exp_scores,axis=1,keepdims=True)
    return np.argmax(probs,axis=1)
model=build_model(50,print_loss=True)
plot_decision_boundary(lambda x:predict(model,x))
plt.scatter(x[:,0],x[:,1],s=40,c=y,cmap=plt.cm.Spectral)
plt.show()
