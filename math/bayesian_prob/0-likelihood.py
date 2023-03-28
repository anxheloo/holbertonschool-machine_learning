import numpy as np
''' '''


def likelihood(x,n,P):
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
        
    for i in P:
        if i > 1 or i <0:
            raise ValueError("....")
            
    factorial = np.math.factorial
    
    return (factorial(n) / (factorial(n-x) * factorial(x))) * (P**x) * ((1 - P) ** (n-x))



