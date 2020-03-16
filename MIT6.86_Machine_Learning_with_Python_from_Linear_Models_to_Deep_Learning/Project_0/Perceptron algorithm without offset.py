import numpy as np

X= np.array([[-1,0],[0,1]])

y= np.array([1,1])

theta = [0,0]

def perceptron_origin(X, y):
    theta = np.zeros(len(X[0]))
    T = 10 #this is the iteration

    for t in range(T):
        for i, x in enumerate(X):
            if (np.dot(X[i],theta)*y[i])<=0:
                theta = theta + X[i]*y[i]
                print(theta)
    return theta

theta = perceptron_origin(X,y)
