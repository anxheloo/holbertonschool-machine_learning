import math
import numpy as np 
#!/usr/bin/env python3
""" defines Normal class that represents normal distribution """

class Binomial:
    """class that represents normal distribution"""


    def __init__(self, data=None, n=1 , p=0.5):
        """class constructor""" 
        
        self.n = int(n)
        self.p = float(p)
        
        if self.n <= 0:
            raise ValueError("n must be a positvice value")
            
        if p <= 0 or p >=1:
             raise ValueError("p must be greater than 0 and less than 1")
                
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            
            mean = float(sum(data) / len(data))
            
            summation = 0
            
            for x in data:
                summation += ((x - mean) ** 2)
            
            variance = (summation / len(data))
            
            q = variance / mean
            p = (1 - q)
            n = round(mean / p)
            p = float(mean / n)
            
            self.n = n
            self.p = p
            
            
    def pmf(self,k):
        """A class Exponential that represents a Exponential distribution"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        else:
            return(math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k)))
        
    def cdf(self,k):
        k = int(k)
        if k < 0:
            return 0
#         elif k>= self.n:
#             return 1
#         else:
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
            
            
np.random.seed(0)
data = np.random.binomial(50, 0.6, 100).tolist()
b1 = Binomial(data)
print('n:', b1.n, "p:", b1.p)

b2 = Binomial(n=50, p=0.6)
print('n:', b2.n, "p:", b2.p)

print()


np.random.seed(0)
data = np.random.binomial(50, 0.6, 100).tolist()
b1 = Binomial(data)
print('P(30):', b1.pmf(30))

b2 = Binomial(n=50, p=0.6)
print('P(30):', b2.pmf(30))


print()

np.random.seed(0)
data = np.random.binomial(50, 0.6, 100).tolist()
b1 = Binomial(data)
print('F(30):', b1.cdf(30))

b2 = Binomial(n=50, p=0.6)
print('F(30):', b2.cdf(30))
