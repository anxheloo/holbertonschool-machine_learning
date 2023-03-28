import numpy as np

def mean_cov(X):
    #check conditions
    if not isinstance(X, np.ndarray) or X.ndim !=2:
        raise TypeError("X must be a 2D numpy.ndarray")
    
    
    n,d = X.shape
    
    if n < 2 : 
        raise ValueError("X must contain multiple data points")
    
    
    mean = np.mean(X, axis = 0)
    cov = np.zeros((d, d))
    
    for i in range(n):
        cov += np.outer((X[i] - mean), (X[i] - mean))
        
    cov /= n-1
    
    return (mean.reshape(1, d), cov)
