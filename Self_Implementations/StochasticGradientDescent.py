<<<<<<< HEAD
import numpy as np 

x_data = np.array([1, 2, 3, 4, 5])
y_data = x_data^2 + np.random.normal()


def forward(x, w):
    return(x*w)

def loss(x, y, w):
    y_pred = forward(x, w)
    L = (y_pred - y)*(y_pred - y)
    return(L)

def gradient(x, y, w):
    g = 2*x*(forward(x,w) - y)
    return(g)

def SGD(x, y, alpha=0.001, iter=1000):
    w = 1
    L = [0]*iter 

    for i in range(iter):
        for x, y in zip(x_data, y_data):
            # Step for each data point
            grad = gradient(x, y, w)
            w = w - alpha*grad
            L.append(loss(x, y, w))
    return(w, L)

w, L = SGD(x, y)
=======
import numpy as np 

x_data = np.array([1, 2, 3, 4, 5])
y_data = x_data^2 + np.random.normal()


def forward(x, w):
    return(x*w)

def loss(x, y, w):
    y_pred = forward(x, w)
    L = (y_pred - y)*(y_pred - y)
    return(L)

def gradient(x, y, w):
    g = 2*x*(forward(x,w) - y)
    return(g)

def SGD(x, y, alpha=0.001, iter=1000):
    w = 1
    L = [0]*iter 

    for i in range(iter):
        for x, y in zip(x_data, y_data):
            # Step for each data point
            grad = gradient(x, y, w)
            w = w - alpha*grad
            L.append(loss(x, y, w))
    return(w, L)

w, L = SGD(x, y)
>>>>>>> first commit
