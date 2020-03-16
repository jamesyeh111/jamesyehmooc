import numpy as np

X= np.array([[-4,2],[-2,1], [-1, -1], [2,2],[1,-2]])

y= np.array([1,1,-1,-1, -1])



def perceptron_offset(X, y):
    #theta = np.zeros(len(X[0]))
    theta = [-3,3]
    T = 20 #this is the iteration
    theta_0 = -3
    
    for t in range(T):
        for i, x in enumerate(X):
            if ((np.dot(X[i],theta)+theta_0)*y[i])<=0:
                theta = theta + X[i]*y[i]
                theta_0 = theta_0 + y[i]
                print(theta)
                print(theta_0)
    return theta, theta_0
perceptron_offset(X,y)