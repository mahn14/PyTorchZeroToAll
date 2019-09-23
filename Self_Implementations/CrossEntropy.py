<<<<<<< HEAD
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder

# Forward Function
def function(x, w):
    return(x*w)

# Softmax
def softmax(x, w):

    # apply forward function
    x = function(x, w)

    # calculate p distribution using Softmax equation
    C = np.max(x)
    exps = np.exp(x - C) 
    sm = exps / np.sum(exps)

    return(sm)

# One-Hot-Encode on target variable
def encode_y(y):
    enc = OneHotEncoder(handle_unknown='ignore')
    Y = enc.fit_transform(y.reshape(-1,1))
    return(Y)

# Cross Entropy Loss
def cross_entropy(x, y, w):
    '''
        @params
            x :: single observation
            y :: one-hot-encoded target variable for x
            w :: weights
    '''
    # softmax prob distr for obs x
    p = softmax(x, w)
        
    # CE Loss
    loss_vector = y * np.log(p)
    Loss = -np.sum(loss_vector)
    return(Loss)
   



# Example DATA
X = np.array([[1,5,1], [1,4,2], [2,7,3], [2,10,4]])
y = np.array([1,2,3])
w = [1,1,1]
Y = encode_y(y)
cross_entropy(X[1], Y[1], w)
=======
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder

# Forward Function
def function(x, w):
    return(x*w)

# Softmax
def softmax(x, w):

    # apply forward function
    x = function(x, w)

    # calculate p distribution using Softmax equation
    C = np.max(x)
    exps = np.exp(x - C) 
    sm = exps / np.sum(exps)

    return(sm)

# One-Hot-Encode on target variable
def encode_y(y):
    enc = OneHotEncoder(handle_unknown='ignore')
    Y = enc.fit_transform(y.reshape(-1,1))
    return(Y)

# Cross Entropy Loss
def cross_entropy(x, y, w):
    '''
        @params
            x :: single observation
            y :: one-hot-encoded target variable for x
            w :: weights
    '''
    # softmax prob distr for obs x
    p = softmax(x, w)
        
    # CE Loss
    loss_vector = y * np.log(p)
    Loss = -np.sum(loss_vector)
    return(Loss)
   



# Example DATA
X = np.array([[1,5,1], [1,4,2], [2,7,3], [2,10,4]])
y = np.array([1,2,3])
w = [1,1,1]
Y = encode_y(y)
cross_entropy(X[1], Y[1], w)
>>>>>>> first commit
