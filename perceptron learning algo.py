import numpy as np
class perceptron(object):
    '''
    parameters :
        eta=learning rate (0-1)(float)
        n_iter=iterations or passes (int)
        _______________
        attributes:
        w_= updated weights(1 dimensional array)
        errors=number of misclassifications in each epoch(list)
        #epoch =max. numnber of iterations
        '''
def __init__(self,eta=.01,n_iter=10):
    self.eta=eta
    self.n_iter=n_iter
def fit(self,x,y):
    '''
parameters:
x : {array-like}, shape = [n_samples, n_features]
 Training vectors, where n_samples
 is the number of samples and
  y :  array-like, shape = [n_samples]
 Target values.
 Returns
 -------
 self : object
 '''
    self.w_=np.zeros(1+x.shape[1])
    self.errors_=[]
    for i in range(self.n_iter):
        errors=0
        
