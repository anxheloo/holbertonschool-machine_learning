import numpy as np
    
class MultiNormal:
    
    def __init__(self, data):
        
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        
        n, d = data.shape
        
        if n < 2:
            raise ValueError("data must contain multiple data points")
        
        self.mean = np.mean(data, axis=0).reshape(d, 1)
        
        self.cov = np.zeros((d, d))
        
        for i in range(d):
            for j in range(d):
                self.cov[i][j] = np.sum((data[:,i]-self.mean[i])*(data[:,j]-self.mean[j])) / (n-1)
                
                

    def pdf(self, x):
        
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        
        d, _ = self.mean.shape
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")
        
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        expo = -0.5 * ((x - self.mean).T @ inv @ (x - self.mean))
        coeff = 1 / (np.sqrt((2*np.pi)**d * det))
        
        return coeff * np.exp(expo)
        
