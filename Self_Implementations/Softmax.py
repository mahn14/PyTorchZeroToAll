<<<<<<< HEAD
import numpy as np 


''' Softmax Function returns vector of probabilities'''
def softmax(X):
    C = np.max(X)
    exps = np.exp(X - C) 
    sm = exps / np.sum(exps)

    return(sm)


def cross_entropy(X,y):
    p = softmax(X)
    CE = -np.sum(y*np.log(p)) / len(y)

    return(CE)


def delta_cross_entropy(X,y):
    m = len(y)
    grad = softmax(X)
    grad[range(m),y] -= 1
    grad = grad / m

=======
import numpy as np 


''' Softmax Function returns vector of probabilities'''
def softmax(X):
    C = np.max(X)
    exps = np.exp(X - C) 
    sm = exps / np.sum(exps)

    return(sm)


def cross_entropy(X,y):
    p = softmax(X)
    CE = -np.sum(y*np.log(p)) / len(y)

    return(CE)


def delta_cross_entropy(X,y):
    m = len(y)
    grad = softmax(X)
    grad[range(m),y] -= 1
    grad = grad / m

>>>>>>> first commit
    return(grad)