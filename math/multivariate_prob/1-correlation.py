import numpy as np
from math import *

def correlation(C):
    #check conditions
    
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
        
    if C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
        
    d = C.shape[0]
    
    corr = np.zeros((d,d))
    
    for i in range(d):
        for j in range(d):
            corr[i][j] = C[i][j] / np.sqrt(C[i][i] * C[j][j])
            
    return corr
    
#     D = sqrt(np.diag(C))
#     D_inverse = 1/ np.outer(D, D)
    
#     corr = D_inverse * C
    
#     return corr
    
