import numpy as np
''' '''


def posterior(x,n,P,Pr):
    ''' 
    '''
    if type(n) is not int or n<=0:
        raise ValueError("n must be a positive integer")
    
    if type(x) is not int or x < 0:
        raise ValueError("x must be an integer")
        
    if x > n:
        raise ValueError("x cannot be grater than n")
    
    if type(P) is not np.ndarray or len(P.shape) != 1:
        raise TypeError("....")
        
    if type(Pr) is not np.ndarray or Pr.shape != P.shape:
        raise TypeError("....")
        
    for i in range(P.ndim):
        if P[i] > 1 or P[i] <0:
            raise ValueError("....")
            
        if Pr[i] > 1 or Pr[i] <0:
            raise ValueError("....")
            
    if np.isclose([np.sum(Pr)], [1]) == [False]:
        raise ValueError(".....")
            
    factorial = np.math.factorial
    
    likelihood = (factorial(n) / (factorial(n-x) * factorial(x))) * (P**x) * ((1 - P) ** (n-x))
    
    intersection = likelihood * Pr
    
    #Marginal
    marginal = np.sum(intersection)
    
    #Posterior
    posterior = intersection / marginal
    
    return posterior



